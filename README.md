<h1 align="center">HumbleRush</h1>
<p align="center">A powerful tool for <a href="https://rumblerush.io">Rumble Rush</a> by PocketHaven.</p>


# 📚 Table of Contents

- 🌟 [Features](#features)
- ⚙️ [Setup](#setup)
- 🔑 [Obtaining Refresh Token](#obtaining-refresh-token)
- ⚠️ [Disclaimer](#disclaimer)

#  <a id="features"></a>🌟 Features

- Boost trophies (10 per request)
- Claim rewards from trophy paths (currency and lootboxes)
  - Lootboxes don't get credited to your account through this requests-based method.
- Automatically upgrade all power-ups
- Set a custom time for timed trial leadeboards
  - This works on **ANY** username.
    - If you're not using it on your own username, it will set *your* personal best to the given time but the world record will go to the username you entered.
    - This means you can use **your own account** to shift anyone else's position on the time trial leaderboards (by incrementing).
- Set a nickname longer than 12 characters server-side.
  - This nickname will be shown everywhere. However, in-game, others will see your name with a trailing "..." after the first 12 characters.
  - Bypasses language checks and allows spaces
- Spoof daily quests and claim their rewards

## 📝 TODO
- [x] Use refresh token to obtain the token instead, eliminates the need to manually obtain the token every hour.
- [x] Spoof practice modes to get on top of time trial leaderboards.
- [x] Bypass the 12 character username limit to the server-side.

# <a id="setup"></a>⚙️ Setup

> [!WARNING]
> Before you run HumbleRush, you first need to obtain your refresh token.

```plaintext
git clone https://github.com/NoobToolzz/HumbleRush.git && cd HumbleRush
pip install -r requirements.txt
python main.py
```

# <a id="obtaining-refresh-token"></a>🔑 Obtaining Refresh Token

1. Head to [rumblerush.io](https://rumblerush.io) and press `CTRL + SHIFT + I`, and go to the “Network” tab in the developer tools.
2. In the filter/search bar, enter “securetoken.”
3. Look for the **POST** request to `securetoken.googleapis.com` and click it.
4. Head to the "Request" tab in the opened panel and copy the `refresh_token` value.
5. Upon startup, you'll be prompted to enter the refresh token.

![Steps](data/attachments/steps.png)

# <a id="disclaimer"></a>⚠️ Disclaimer

I want to make it clear that I am not responsible for any consequences resulting from your use of HumbleRush to cheat in Rumble Rush. By using this tool, you acknowledge that you do so at your own risk and understand the potential consequences.
