import datetime
import discord
from discord.ext import commands
from utils.helpers import *

log_channel = 1468248316235219065

class SniperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})

    

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        if not isAllowedInGuild(self,message.guild.id): 
            return
        
        if message.author.bot:
            return

        if not message.content and not message.attachments:
            return

        embed = discord.Embed(
            title="",
            description=message.content if message.content else "*[No text content]*",
            color=0xff4747,
            timestamp=message.created_at
        )

        embed.set_author(
            name=f"{message.author.display_name} ({message.author.id})",
            icon_url=message.author.display_avatar.url
        )

        if message.attachments:
            embed.set_image(url=message.attachments[0].url)
            embed.add_field(name="Attachments", value=f"{len(message.attachments)} file(s) attached")

        await message.channel.send(content=f"**{message.author.mention} deletin messages**", embed=embed)

        # send the same embed to the logs channel, but edit the embed to also add in the channel that it was deleted from
        logs = self.bot.get_channel(log_channel)
        if logs:
            # We add the channel info specifically for the logs
            embed.add_field(name="Channel", value=message.channel.mention, inline=False)
            await logs.send(embed=embed)


async def setup(bot):
    await bot.add_cog(SniperCog(bot))
