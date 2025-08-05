import requests
from rich import print


def purchaseItemUpgrade(headers):
    while True:
        response = requests.post(
            "https://us-central1-pocketrun-33bdc.cloudfunctions.net/v0240_items_upgrade/purchaseItemUpgrade",
            headers=headers,
            json={"purchaseId": "items_upgrade_coins"},
        )

        if response.status_code == 200:
            data = response.json()
            print(
                f"[bold green]Upgraded {data['rewardClaimResults'][0]['originalReward']['id']}[/bold green]"
            )
        elif "user doesn't have enough currency".lower() in response.text:
            print("[bold red]Not enough currency, stopping[/bold red]")
            break
        else:
            print(f"[bold red]Error {response.text}[/bold red]")
