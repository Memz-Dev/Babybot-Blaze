import asyncio
import discord
from discord.ext import commands
from utils.helpers import *
import random

reportChannelID = 1493554983235227719
reactions = ["👍","👎","😂","‼️",]

class NewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self, {1347246964865105972})

    @commands.command()
    async def report(self, ctx, headline: str, *, body: str):
        if not isAllowedInGuild(self, ctx.guild.id): 
            return
        
        if not await author_is_owner(ctx):
            return

        target_channel = self.bot.get_channel(reportChannelID)
        if not target_channel:
            return await ctx.send("Error: I couldn't find the reporting channel.")

        embed = discord.Embed(
            title=headline,
            description=body,
            color=0x4f90f7,
        )

        if ctx.message.attachments:
            attachment_url = ctx.message.attachments[0].url
            embed.set_image(url=attachment_url)
        
        embed.set_footer(text=f"Reported by {ctx.author.display_name}")
        embed.timestamp = ctx.message.created_at

        post = await target_channel.send(embed=embed)
        for emoji in reactions:
            await post.add_reaction(emoji)

async def setup(bot):
    await bot.add_cog(NewsCog(bot))