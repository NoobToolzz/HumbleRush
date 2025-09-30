import requests
from rich import print
from data import get_full_url
from datetime import datetime


class QuestUtilities:
    def __init__(self):
        self.day = datetime.now().strftime("%A").lower()

    def progressQuests(self, headers):
        try:
            r = requests.post(
                get_full_url("progressQuests"),
                headers=headers,
                json={
                    "questsToProgress": {
                        "DailyQuests": {
                            f"quests.daily.{self.day}.1": 999.0,
                            f"quests.daily.{self.day}.2": 999.0,
                            f"quests.daily.{self.day}.3": 999.0,
                        }
                    }
                },
            )

            if r.status_code == 200:
                print("[bold green]Successfully spoofed daily quests!")
                print("[cyan]Claiming quest rewards...")
                self.claimQuestRewards(headers)
            else:
                print(f"[bold red]Failed to spoof daily quests: {r.text}")
        except Exception as e:
            print(f"[bold red]Unknown exception occured when spoofing quests: {e}")

    def claimQuestRewards(self, headers):
        try:
            for i in range(1, 4):
                r = requests.post(
                    get_full_url("claimQuestReward"),
                    headers=headers,
                    json={
                        "questCategory": "DailyQuests",
                        "questId": f"quests.daily.{self.day}.{i}",
                    },
                )

                if r.status_code == 200:
                    print(f"[bold green]Successfully claimed quest {i} rewards!")
                else:
                    print(f"[bold red]Failed to claim quest {i} rewards: {r.text}")
        except Exception as e:
            print(f"[bold red]Unknown exception occured when claiming rewards: {e}")
