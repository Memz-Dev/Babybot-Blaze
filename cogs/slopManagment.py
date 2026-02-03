import discord
from discord.ext import commands
from utils.helpers import *
import time

class SlopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})

        self.purgatoryCooldown = 60
        self.purgatoryTimestamp = time.time() - self.purgatoryCooldown

    

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
            await announce_slopped_member(self.bot,member)


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
            await announce_slopped_member(self.bot,member)

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
                    await announce_slopped_member(self.bot,member)
                except Exception as e:
                    print(f"Could not re-slop {member.name}: {e}")

    @commands.command()
    async def releasethelist(self, ctx):
        if not isAllowedInGuild(self, ctx.guild.id):
            return
        
        ids = get_list()  # list of user IDs

        names = []
        for uid in ids:
            names.append(f"<@{uid}>")

        final_text = "\n".join(names) if names else "none, shibal list empty"

        embed = discord.Embed(
            title="The purgatory list",
            color=0x00FF00
        )
        embed.add_field(
            name="All slopped members:",
            value=final_text,
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['pm'])
    async def purgatorymessage(self, ctx, *, message: str = None):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        
        #if ctx.author.id != 524292628171325442:
        #   await ctx.send("stupid bitch member")
        #   return

        channel = self.bot.get_channel(1348640981586808882)
        if channel is None:
            return

        if not message:
            return await ctx.send("where msg retard")
        
        timePassed = time.time() - self.purgatoryTimestamp
        if timePassed < self.purgatoryCooldown:
            return await ctx.send(f"be patient bitch - {round(self.purgatoryCooldown - timePassed)} seconds")

        self.purgatoryTimestamp = time.time()

        await channel.send(f"{message}\n*- {ctx.author.name}*")
        await ctx.send("vr vr good, message sent")
        


async def setup(bot):
    await bot.add_cog(SlopCog(bot))
