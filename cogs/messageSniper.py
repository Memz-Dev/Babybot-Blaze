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
        
        if message.guild is None:
            return
        
        deleter = message.author

        async for entry in message.guild.audit_logs(action=discord.AuditLogAction.message_delete, limit=1):
            # Check if the log entry matches the message author and happened recently
            if entry.target == message.author:
                deleter = entry.user
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

        if deleter.id == message.author.id:
            await message.channel.send(content=f"**{message.author.mention} deletin messages**", embed=embed)

        logs = self.bot.get_channel(log_channel)
        if logs:
            embed.add_field(name="Channel", value=message.channel.mention, inline=False)
            await logs.send(embed=embed)


async def setup(bot):
    await bot.add_cog(SniperCog(bot))
