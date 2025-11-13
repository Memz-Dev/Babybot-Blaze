import asyncio
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

worhtless_value_to_update = 4

async def main():
    # await load_extension because load_extension is coroutine in modern discord.py
    await bot.load_extension("cogs.slopManagment")
    await bot.load_extension("cogs.general")
    await bot.load_extension("cogs.autoresponse")
    await bot.load_extension("cogs.botstatus")
    print("Starting bot")
    
    # use start() instead of run()
    await bot.start(TOKEN)

asyncio.run(main())
