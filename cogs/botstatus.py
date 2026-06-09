import discord
import requests
from discord.ext import commands
from utils.helpers import *
import subprocess


version = "-"



class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        @bot.event
        async def on_ready():
            await bot.change_presence(activity=discord.Game(name=f"Version {get_local_version()}"))

        @bot.command()
        async def version(ctx):
            if ctx.author.id != owner_id:
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
                    description=f"Version: `{local}` (Latest)",
                    color=0x00FF00
                )
                await ctx.send(embed=embed)
                return
            
            if local == "dev-000":
                embed = discord.Embed(
                    title="Running locally",
                    description=f"Latest: `{remote}`",
                    color=0x00FF00
                )
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(
                    title="Running online",
                    description=f"Version: `{local}` (Behind)\nLatest: `{remote}`",
                    color=0x00FF00
                )
            await ctx.send(embed=embed)

        @bot.command()
        async def update(ctx):
            if ctx.author.id != Sigma_ID:
                await ctx.send("stupid bitch member")
                return
            
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

            await ctx.send(f"Updating to `{remote}`")

            output = subprocess.getoutput(UPDATE_SCRIPT)
            embed = discord.Embed(
                title="Update complete!",
                description=f"New version: `{remote}`\n{output}",
                color=0x00FF00
            )
            await ctx.send(embed=embed)
            restartOutput = subprocess.getoutput(RESTART_SCRIPT)

        @bot.command()
        async def updateproto(ctx):
            if ctx.author.id != Sigma_ID:
                await ctx.send("stupid bitch member")
                return
            
            
            output = subprocess.getoutput(f"sudo /home/memz/Proto/update_bot.sh")
            embed = discord.Embed(
                title="Update complete!",
                description=f"{output}",
                color=0x00FF00
            )
            await ctx.send(embed=embed)
            
                
            
            
        
    


async def setup(bot):
    await bot.add_cog(StatusCog(bot))
