import requests
from rich import print
from data import get_full_url
from rich.prompt import Prompt


class TimeTrialSpoofer:
    def __init__(self):
        self.map_codes = {
            "Block Survival (Neon)": "block_survival",
            "Block Survival (Island)": "block_survival_2",
            "Castle Bash": "castle_bash",
            "Neon Dash Blast": "neo_dash_blast",
            "Island Adventure": "island_adventure",
            "Space Station 14": "space_station_14",
            "Sky Rail City": "sky_rail_city",
            "Meltdown Mines": "meltdown_mines",
            "Ultimate Runner": "ultimate_spinner",
            "Steampunk Spinner": "steampunk_spinner",
            "Meltdown Mines": "meltdown_mines",
            "Pipeworks Panic": "pipeworks_panic",
            "Starfield Nebula": "starfield_nebula",
        }

    def isEliminationMode(self, map):
        return map in [
            "block_survival",
            "block_survival_2",
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
            get_full_url("setBestTime"),
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
                f"[bold green]Successfully set the best time of {time}s for [bold yellow]{username}[/bold yellow]!"
            )
        else:
            print(f"[bold red]Error: {response.text}")
