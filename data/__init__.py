BASE_URL = "https://us-central1-pocketrun-33bdc.cloudfunctions.net"
API_VERSION = "v0280"
# Sorted by endpoint:type
TYPES = {
    "nickname": "player",
    "matchEnd": "player",
    "claimReward": "ranks",
    "setBestTime": "maps",
    "purchaseItemUpgrade": "items_upgrade",
    "progressQuests": "quests",
    "claimQuestReward": "quests",
}


def get_full_url(endpoint):
    return f"{BASE_URL}/{API_VERSION}_{TYPES.get(endpoint)}/{endpoint}"
