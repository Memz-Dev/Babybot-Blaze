import asyncio
import discord
from discord.ext import commands
from utils.helpers import *
import random

# The ID for the channel where the news will be posted
reportChannelID = 1493554983235227719
reactions = ["👍","👎","😂","‼️",]

class NewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self, {1347246964865105972})

    @commands.command()
    async def report(self, ctx, headline: str, *, body: str):
        """
        Usage: !report "This is the headline" This is the rest of the body text.
        Note: Wrap the headline in quotes if it has multiple words.
        """
        if not isAllowedInGuild(self, ctx.guild.id): 
            return
        
        if not await author_is_owner(ctx):
            return

        # 1. Grab the target channel
        target_channel = self.bot.get_channel(reportChannelID)
        if not target_channel:
            return await ctx.send("Error: I couldn't find the reporting channel.")

        # 2. Create the Embed
        # You can change the color (e.g., discord.Color.blue())
        embed = discord.Embed(
            title=headline,
            description=body,
            color=0x4f90f7,
        )

        if ctx.message.attachments:
            # Grab the first attachment and set it as the embed image
            attachment_url = ctx.message.attachments[0].url
            embed.set_image(url=attachment_url)
        
        # Adding a timestamp and footer for a more "official" look
        embed.set_footer(text=f"Reported by {ctx.author.display_name}")
        embed.timestamp = ctx.message.created_at

        # 3. Send and give feedback
        post = await target_channel.send(embed=embed)
        for emoji in reactions:
            await post.add_reaction(emoji)

async def setup(bot):
    await bot.add_cog(NewsCog(bot))