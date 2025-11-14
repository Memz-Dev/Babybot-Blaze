import discord
from discord.ext import commands
from utils.helpers import *

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})

    @commands.command()
    async def commands(self, ctx, member: discord.Member = None):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        
        await ctx.send("!slopmeplease")

    @commands.command()
    async def album(self, ctx):
        await ctx.send(get_release(774670))


async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
