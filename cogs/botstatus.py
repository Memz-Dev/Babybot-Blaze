import discord
import requests
from discord.ext import commands
from utils.helpers import *
import subprocess

Sigma_ID = 524292628171325442
REPO_API = "https://api.github.com/repos/memz-dev/babybot-blaze/branches/main"

version = "-"

def get_local_version():
    with open(".version") as f:
        version = f.read().strip()
    return version
    
BOT_PATH = "/home/memz/Babybot-Blaze"
UPDATE_SCRIPT = f"{BOT_PATH}/update_bot.sh"
RESTART_SCRIPT = f"{BOT_PATH}/restart.sh"
VERSION_FILE = f"{BOT_PATH}/.version"

def get_remote_version():
    resp = requests.get(REPO_API)
    resp.raise_for_status()
    data = resp.json()
    return data["commit"]["sha"][:7]  # short hash

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        @bot.event
        async def on_ready():
            await bot.change_presence(activity=discord.Game(name=f"Version {get_local_version()}"))

        @bot.command()
        async def version(ctx):
            if ctx.author.id != Sigma_ID:
                await ctx.send("stupid bitch member")
                return

            local = get_local_version()
            try:
                remote = get_remote_version()
            except Exception as e:
                await ctx.send(f"fumble: {e}")
                return

            if local == remote:
                embed = discord.Embed(
                    title="Running online",
                    description=f"Version: {local} (Latest)",
                    color=0x00FF00
                )
                await ctx.send(embed=embed)
                return
            
            if local == "dev-000":
                embed = discord.Embed(
                    title="Running locally",
                    description=f"Latest: {remote}",
                    color=0x00FF00
                )
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(
                    title="Running online",
                    description=f"Version: {local} (Behind)\nLatest: {remote}",
                    color=0x00FF00
                )
            await ctx.send(embed=embed)

        @bot.command()
        async def update(ctx):
            local = get_local_version()

            if local == "dev-000":
                await ctx.send("stupid bitch you're local")
                return

            try:
                remote = get_remote_version()
            except Exception as e:
                await ctx.send(f"fumble: {e}")
                return
            
            if local == remote:
                await ctx.send("already on latest version bitch")
                return

            embed = discord.Embed(
                title="Updating",
                description=f"Updating to `v{remote}`",
                color=0x00FF00
            )
            await ctx.send(embed=embed)

            await ctx.send(subprocess.getoutput(UPDATE_SCRIPT))
            #await ctx.send(f"update complete!\nNew version: {get_local_version()}\nRestarting...")
            await ctx.send(subprocess.getoutput(RESTART_SCRIPT))
                
            
            
        
    


async def setup(bot):
    await bot.add_cog(StatusCog(bot))
