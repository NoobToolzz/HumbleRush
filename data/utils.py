import requests
import json
from rich import print
from rich.prompt import Prompt
from datetime import datetime, timedelta
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class Utils:
    def __init__(self):
        self.config = self.load_config()
        self.user_agent_rotator = self.get_user_agent_rotator()

    def load_config(self):
        with open("config.json") as file:
            return json.load(file)

    def set_config(self, key, value):
        self.config[key] = value

        with open("config.json", "w") as file:
            json.dump(self.config, file, indent=4)

    # Checks if "refresh_token" is filled correctly and proceeds to refresh token every 1h (not each startup since that's essentially pointless requests)
    def startup_checks(self):
        current_time = datetime.now().isoformat()
        last_refresh = self.config["last_refresh_timestamp"]

        # Get the refresh token if it exists in the config
        refresh_token = self.config["refresh_token"] or Prompt.ask(
            "Enter your refresh token"
        )
        self.set_config("refresh_token", refresh_token)

        if last_refresh == "" or (
            datetime.fromisoformat(current_time) - datetime.fromisoformat(last_refresh)
            > timedelta(hours=1)
        ):  # Make sure to refresh the access token every hour.
            print("[bold green]Refreshing access token")
            self.refresh_access_token()

            self.set_config("last_refresh_timestamp", current_time)

    def get_user_agent_rotator(self):
        return UserAgent(
            software_names=[SoftwareName.CHROME.value, SoftwareName.FIREFOX.value],
            operating_systems=[
                OperatingSystem.WINDOWS.value,
                OperatingSystem.LINUX.value,
                OperatingSystem.MACOS.value,
            ],
            limit=1,
        )

    def get_headers(self):
        return {
            "Host": "us-central1-pocketrun-33bdc.cloudfunctions.net",
            "User-Agent": self.user_agent_rotator.get_random_user_agent(),
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://rumblerush.io/",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config["access_token"]}",
            "Content-Length": "59",
            "Origin": "https://rumblerush.io",
            "Sec-GPC": "1",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "DNT": "1",
            "Priority": "u=4",
            "TE": "trailers",
        }

    def refresh_access_token(self):
        response = requests.post(
            "https://identitytoolkit.googleapis.com/v1/token?key=AIzaSyDyBOKTSOCMvzJJsaf14eU9SezR0B12uPs",  # Yes, they had their API key in the URL params
            headers={"Content-Type": "application/json"},
            json={
                "grant_type": "refresh_token",
                "refresh_token": str(self.config["refresh_token"]),
            },
        )

        if response.status_code == 200:
            self.set_config("access_token", response.json().get("access_token"))
        else:
            print(
                f"[bold red]Error refreshing access token. 'refresh_token' in config may have expired/been invalidated. Response: {response.json()}"
            )
