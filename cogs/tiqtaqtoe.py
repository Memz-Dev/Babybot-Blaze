import discord
from discord.ext import commands
from utils.helpers import *
import random

class TTTCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1415255360473796692})

    

    @commands.command()
    async def kiesgoon(self, ctx, *, message: str = None):
        if not isAllowedInGuild(self, ctx.guild.id):
            return

        members = [m for m in ctx.guild.members if not m.bot]
        member = random.choice(members)

        await ctx.send(f"{member.mention} {message or ''}")

    



async def setup(bot):
    await bot.add_cog(TTTCog(bot))
