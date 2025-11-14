import discord
from discord.ext import commands
from utils.helpers import *

class MessAroundCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #setAllowedGuilds(self,{1347246964865105972})

    @commands.command()
    async def dm(self, ctx, member: discord.Member = None, *, message: str = None):
        if not await author_is_owner(ctx):
            return

        if not await member_is_mentioned(member, ctx):
            return

        if message is None:
            await ctx.send("waoww… you no give message??")
            return

        try:
            await member.send(message)
            await ctx.send("haha i dm")
        except:
            await ctx.send("i fumble uhghhh")



async def setup(bot):
    await bot.add_cog(MessAroundCog(bot))
