import discord
from discord.ext import commands
from utils.helpers import *

class SlopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})

    @commands.command()
    async def slopthisman(self, ctx, member: discord.Member = None):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return

        if not await quick_check_roleEdit(ctx):
            return
        
        if not await member_is_mentioned(member,ctx):
            return
        
        if await slop_member(ctx,member) == True:
            await ctx.send(f"{member.mention} haha bitch member slop")


    @commands.command()
    async def freethisman(self,ctx, member: discord.Member = None):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        
        if not await quick_check_roleEdit(ctx):
            return
        
        if not  await member_is_mentioned(member,ctx):
            return
        
        if await unslop_member(ctx,member) == True:
            await ctx.send(f"{member.mention} wow free")  

    @commands.command()
    async def slopmeplease(self, ctx):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        
        role = ctx.guild.get_role(slopperRole)
        member = ctx.author

        if await slop_member(ctx,member) == True:
            await ctx.send(f"{member.mention} wow self slop")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not isAllowedInGuild(self,member.guild.id): 
            return

        # check if this member was previously given the slop role
        if member.id in stored_members:
            role = member.guild.get_role(slopperRole)
            if role:
                try:
                    await member.add_roles(role)
                except Exception as e:
                    print(f"Could not re-slop {member.name}: {e}")

async def setup(bot):
    await bot.add_cog(SlopCog(bot))
