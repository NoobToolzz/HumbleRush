import requests
import threading
import time
from rich import print


def claim_trophy(count, headers):
    response = requests.post(
        "https://us-central1-pocketrun-33bdc.cloudfunctions.net/v0240_player/matchEnd",
        headers=headers,
        json={"modeType": "Tournament", "place": 1, "challenges": None},
    )

    if response.status_code == 200:
        print(f"[green]Request {count + 1} was successful.[/green]")
    else:
        print(f"[red]Error: {response.status_code} - {response.text}[/red]")


def claim_trophies(num_requests, num_threads, headers):
    threads = []
    count = 0

    while count < num_requests or num_requests == float("inf"):
        if num_threads > 1:
            thread = threading.Thread(target=claim_trophy, args=(count, headers))
            threads.append(thread)
            thread.start()
        else:
            claim_trophy(count, headers)

        count += 1
        time.sleep(0.5)

    if num_threads > 1:
        for thread in threads:
            thread.join()
