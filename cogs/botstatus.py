import discord
from discord.ext import commands
from utils.helpers import *

with open(".version") as f:
    version = f.read().strip()

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        @bot.event
        async def on_ready():
            await bot.change_presence(activity=discord.Game(name=f"Version {version}"))
            print(f"Bot is online, version {version}")
    


async def setup(bot):
    await bot.add_cog(StatusCog(bot))
