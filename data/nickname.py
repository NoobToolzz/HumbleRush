import requests
from rich import print
from data import get_full_url


def setNickname(nickname, headers):
    response = requests.post(
        get_full_url("nickname"),
        headers=headers,
        json={
            "nickname": "".join(char + "\u200B" for char in nickname)
        },  # Zero-width spaces to bypass language checks
    )

    if response.status_code == 200:
        print(f"[bold green]Successfully set your nickname to {nickname}!")
    else:
        print(f"[bold red]Error setting nickname: {response.text}")
