import os
from rich import print
from rich.prompt import Confirm, Prompt
from data.utils import Utils
from data.nickname import setNickname
from data.trophy import claim_trophies
from data.reward import claim_rewards
from data.upgrade import purchaseItemUpgrade
from data.time_trials import TimeTrialSpoofer
from data.quests import QuestUtilities


def main_menu():
    headers = Utils().get_headers()

    print("[bold cyan]Welcome to HumbleRush![/bold cyan]")
    while True:
        print("\n[bold yellow]Please choose an option:[/bold yellow]")
        # print("1. Claim Trophies [PATCHED - DONT USE]")
        print("1. Claim Rewards")
        print("2. Set practice leaderboard time (works on any username)")
        print("3. Purchase item upgrades")
        print("4. Set nickname (bypasses 12 character limit)")
        print("5. Spoof & claim daily quests")
        print("q. Exit")

        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "q"])

        """
        if choice == "1":
            num_requests = Prompt.ask(
                "How many requests? (1 = 10 trophies, leave blank for unlimited)",
            )
            num_requests = int(num_requests) if num_requests.isdigit() else float("inf")
            num_threads = 0

            if Confirm.ask("Use threads?"):
                num_threads = Prompt.ask(
                    "How many threads", default="5", show_default=True
                )
                num_threads = int(num_threads)

            claim_trophies(num_requests, num_threads, headers)
        """

        if choice == "1":
            threads = Prompt.ask("How many threads?", default="5", show_default=True)
            tiers = Prompt.ask("How many tiers do you want to claim?")

            claim_rewards(int(tiers), int(threads), headers)

        elif choice == "2":
            username = Prompt.ask("Enter ANYBODYS username")
            selected_map = TimeTrialSpoofer().chooseMap()
            time = Prompt.ask("Enter the best time in seconds")

            TimeTrialSpoofer().setBestTime(float(time), selected_map, username, headers)

        elif choice == "3":
            purchaseItemUpgrade(headers)

        elif choice == "4":
            nickname = Prompt.ask("Enter your new nickname")

            setNickname(nickname, headers)

        elif choice == "5":
            QuestUtilities().progressQuests(headers)

        elif choice == "q":
            print("[bold green]Exiting the program. Goodbye![/bold green]")
            break


if __name__ == "__main__":
    Utils().startup_checks()  # Makes sure config values are present
    os.system("cls" if os.name == "nt" else "clear")

    main_menu()
