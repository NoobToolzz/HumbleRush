import requests
from rich import print


def setNickname(nickname, headers):
    response = requests.post(
        "https://us-central1-pocketrun-33bdc.cloudfunctions.net/v0240_player/nickname",
        headers=headers,
        json={"nickname": nickname},
    )

    if response.status_code == 200:
        print(f"[bold green]Successfully set your nickname to {nickname}!")
    else:
        print(f"[bold red]Error setting nickname: {response.text}")
