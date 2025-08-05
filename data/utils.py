import requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def read_bearer_token():
    with open("token.txt") as file:
        return file.read().strip()


def get_user_agent_rotator():
    return UserAgent(
        software_names=[SoftwareName.CHROME.value, SoftwareName.FIREFOX.value],
        operating_systems=[
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.MACOS.value,
        ],
        limit=1,
    )


def get_headers(user_agent_rotator):
    return {
        "Host": "us-central1-pocketrun-33bdc.cloudfunctions.net",
        "User-Agent": user_agent_rotator.get_random_user_agent(),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://rumblerush.io/",
        "Content-Type": "application/json",
        "Authorization": f"{read_bearer_token()}",
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
