import re
import requests
from rich import print
from rich.live import Live
from rich.table import Table
from rich.prompt import Prompt, Confirm
from data import get_full_url


class Clans:
    def __init__(self):
        pass  # Idk what to put here as everything requires club IDs and needs headers

    def searchClans(self, query, headers):
        table = Table(title="Clans Search")
        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("ID", justify="left", style="cyan", no_wrap=True)
        table.add_column("Members", justify="left", style="cyan", no_wrap=True)
        table.add_column("Total Trophies", justify="left", style="cyan", no_wrap=True)

        try:
            # The request fails with this header
            del headers["Content-Length"]
            r = requests.get(
                get_full_url("search"), headers=headers, params={"query": query}
            )

            if r.status_code == 200:
                with Live(table, refresh_per_second=4):
                    for clan in r.json():
                        table.add_row(
                            f"{clan['Name']}",
                            f"{clan['id']}",
                            f"{clan['MembersCount']}",
                            f"{clan['TotalTrophies']}",
                        )
            else:
                print(f"[bold red]Error obtaining clans list/list is empty: {r.text}")
                return
        except Exception as e:
            print(f"[bold red]Unknown exception occurred: {e}")

    def getClanData(self, clan_id, headers):
        global clan_name, clan_status

        try:
            del headers["Content-Length"]  # Needed here too
            r = requests.get(
                get_full_url("getClubData"), headers=headers, params={"clubId": clan_id}
            )

            if r.status_code == 200:
                data = r.json()
                clan_name = data["name"]
                clan_status = data["isOpen"]
            else:
                print(f"[bold red]Failed to get clan data: {r.text}")
        except Exception as e:
            print(f"[bold red]Unknown exception occurred: {e}")

        return clan_name, clan_status

    def leaveClub(self, clan_id, headers):
        try:
            r = requests.post(
                get_full_url("leave"), headers=headers, json={"clubId": clan_id}
            )

            if r.status_code == 200:
                print(f"[bold green]Sucessfully left clan '{clan_name}'")
            else:
                print(f"[bold red]Failed to leave clan: {r.text}")
        except Exception as e:
            print(f"Unknown exception occurred: {e}")

    def apply(self, clan_id, nickname, headers):
        if re.match(r"^[A-Z0-9]{8}$", clan_id):  # Clan ID regex matching
            pass
        else:
            print(f"[yellow]Searching for clans with query '{clan_id}'...")
            self.searchClans(clan_id, headers)
            clan_id = Prompt.ask("Enter a Clan ID from search results")

        try:
            headers["Content-Length"] = "45"  # Yes.
            r = requests.post(
                get_full_url("apply"),
                headers=headers,
                json={
                    "clubId": clan_id,
                    "nickname": str(
                        "".join(char + "\u200b" for char in nickname)
                    ),  # Bypass language checks again
                },
            )

            clan_name, clan_status = self.getClanData(clan_id, headers)

            if r.status_code == 200:
                print(f'[bold green]Successfully applied to clan "{clan_name}"')
                if clan_status:
                    print(
                        "[cyan]It looks like the clan is open, you should have now joined the clan."
                    )
                elif not clan_status:
                    print(
                        "[cyan]It looks like your clan requires manual approval from the owner, please be patient."
                    )

                print(
                    "[bold dark_orange]Note: Your spoofed username shows server-side in the clan, you'll see your account username client-side."
                )
            elif "User already in club" in r.text:
                print(f"[bold green]You are already in the clan")
                if Confirm.ask("Continue? (re-applies)"):
                    self.leaveClub(clan_id, headers)
                    self.apply(clan_id, nickname, headers)  # Apply again
                else:
                    return
            else:
                print(f"[bold red]Failed to apply to clan {r.text}")
        except Exception as e:
            print(f"[bold red]Unknown exception occurred: {e}")
