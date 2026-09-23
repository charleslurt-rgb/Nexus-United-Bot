import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv


# ============================================================
# CONFIG
# ============================================================

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set.")


# ============================================================
# INTENTS
# ============================================================

intents = discord.Intents.default()


# ============================================================
# BOT
# ============================================================

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# ============================================================
# LOAD COMMANDS
# ============================================================

async def load_commands():
    commands_path = Path(__file__).parent / "commands"

    for file in commands_path.glob("*.py"):

        if file.name == "__init__.py":
            continue

        extension = f"commands.{file.stem}"

        try:
            await bot.load_extension(extension)
            print(f"Loaded command: {extension}")

        except Exception as error:
            print(f"Failed to load {extension}: {error}")


# ============================================================
# STARTUP
# ============================================================

@bot.event
async def setup_hook():

    await load_commands()

    synced = await bot.tree.sync()

    print(f"Synced {len(synced)} slash commands.")


@bot.event
async def on_ready():

    print("────────────────────────────────")
    print(f"Logged in as: {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Servers: {len(bot.guilds)}")
    print("Nexus United Bot is online.")
    print("────────────────────────────────")


# ============================================================
# RUN
# ============================================================

bot.run(TOKEN)
