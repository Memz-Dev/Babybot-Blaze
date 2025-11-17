import discord
from discord.ext import commands
from utils.helpers import *
import random

class MessAroundCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1415255360473796692})

    

    @commands.command()
    async def kiesgoon(self, ctx, member: discord.Member = None, *, message: str = None):
        if not isAllowedInGuild(self, ctx.guild.id):
            return

        # if no member given, choose random one
        if member is None:
            members = [m for m in ctx.guild.members if not m.bot]
            if not members:
                return await ctx.send("no human here bruh..")
            member = random.choice(members)

        await ctx.send(f"{member.name} {message or ''}")




async def setup(bot):
    await bot.add_cog(MessAroundCog(bot))
