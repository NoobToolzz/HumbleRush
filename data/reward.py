import requests
from rich import print
from concurrent.futures import ThreadPoolExecutor


def claim_reward(tier, headers):
    response = requests.post(
        "https://us-central1-pocketrun-33bdc.cloudfunctions.net/v0240_ranks/claimReward",
        headers=headers,
        json={"tier": tier},
    )

    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and "originalReward" in data[0]:
            reward_type = data[0]["originalReward"]["type"]
            print(f"[bold green]Tier {tier}: {reward_type}[/bold green]")
        else:
            print(f"[bold red]Tier {tier}: No reward found[/bold red]")
    else:
        print(f"[bold red]Tier {tier}: Error {response.status_code}[/bold red]")


def claim_rewards(tiers, threads, headers):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for tier in range(1, tiers + 1):
            executor.submit(claim_reward, tier, headers)
