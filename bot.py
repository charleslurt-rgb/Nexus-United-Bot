import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set.")


# Bot intents
intents = discord.Intents.default()


# Create bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Bot startup
@bot.event
async def on_ready():
    print("────────────────────────────────")
    print(f"Logged in as: {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Servers: {len(bot.guilds)}")
    print("Nexus United Bot is online.")
    print("────────────────────────────────")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as error:
        print(f"Failed to sync commands: {error}")


# Test command
@bot.tree.command(
    name="ping",
    description="Check if the bot is online."
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Pong! `{round(bot.latency * 1000)}ms`"
    )


# Start bot
bot.run(TOKEN)
