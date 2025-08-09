import requests
from rich import print
from rich.prompt import Prompt


class TimeTrialSpoofer:
    def __init__(self):
        self.map_codes = {
            "Block Survival (Neon)": "block_survival",
            "Castle Bash": "castle_bash",
            "Neon Dash Blast": "neo_dash_blast",
            "Island Adventure": "island_adventure",
            "Space Station 14": "space_station_14",
            "Sky Rail City": "sky_rail_city",
            "Meltdown Mines": "meltdown_mines",
            "Ultimate Runner": "ultimate_spinner",
            "Steampunk Spinner": "steampunk_spinner",
        }

    def isEliminationMode(self, map):
        return map in [
            "block_survival",
            "ultimate_spinner",
            "steampunk_spinner",
        ]

    def chooseMap(self):
        print("[bold blue]Available Maps:")
        for index, map_name in enumerate(self.map_codes.keys(), start=1):
            print(f"{index}. {map_name}")

        choice = int(Prompt.ask("[bold yellow]Choose a map by number"))
        map_name = list(self.map_codes.keys())[choice - 1]
        return self.map_codes[map_name]

    def setBestTime(self, time, map, username, headers):
        response = requests.post(
            "https://us-central1-pocketrun-33bdc.cloudfunctions.net/v0240_maps/setBestTime",
            headers=headers,
            json={
                "bestTimeInMillisec": time * 1000,
                "isEliminationMode": self.isEliminationMode(map),
                "isTimeTrial": True,
                "nickname": username,
                "mapId": f"maps.{map}",
            },
        )

        if response.status_code == 200:
            print(
                f"[bold green]Successfully set the best time of {time}s for {username}!"
            )
        else:
            print(f"Error: {response.text}")
