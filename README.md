# Simple Discord Nuke Bot

This is a simple Discord bot that can be used to destroy a server in under 10 seconds. 

## Installation

1. Clone the repository:
```
git clone https://github.com/LukeTheNuke64/Simple-Nuke-Bot.git
```

2. Install the required dependencies:
```
pip install discord.py
```

3. Replace the `BOT_TOKEN` variable with your own Discord bot token.

4. Customize the bot to your preference.

5. Run the bot:
```
python main.py
```

## Usage

The bot has the following commands:

- `!delete`: Deletes all channels in the server.
- `!ban`: Bans all members in a server (excluding the bot and whitelisted users).
- `!start`: Deletes all channels, creates new channels, and spams a message in each channel.
- `!forcestop`: Stops the bot by shutting it down.

#### To use these commands, simply type them in any text channel where the bot has permissions.

Note that the `!start` command can create a large number of channels and send a lot of messages, which may cause issues with Discord's rate limiting. Use this command with caution.
