import time
import requests
import threading
from rich import print
from data import get_full_url


def claim_trophy(count, headers):
    response = requests.post(
        get_full_url("matchEnd"),
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
