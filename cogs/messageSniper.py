import datetime
import discord
from discord.ext import commands
from utils.helpers import *

log_channel = 1468248316235219065


class SniperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self, {1347246964865105972})

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not isAllowedInGuild(self, message.guild.id) or message.author.bot or message.guild is None: 
            return

        if not message.content and not message.attachments:
            return
        
        deleter = message.author
        async for entry in message.guild.audit_logs(action=discord.AuditLogAction.message_delete, limit=1):
            if entry.target == message.author and (datetime.datetime.now(datetime.timezone.utc) - entry.created_at).total_seconds() < 5:
                deleter = entry.user
                break 

        embed = discord.Embed(
            title="Message Deleted",
            description=message.content if message.content else "*[No text content]*",
            color=0xff4747,
            timestamp=discord.utils.utcnow()
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

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not isAllowedInGuild(self, after.guild.id) or after.author.bot or after.guild is None:
            return

        if before.content == after.content:
            return

        embed = discord.Embed(
            title="bro editing",
            color=0x47a0ff,
            timestamp=discord.utils.utcnow(),
            url=after.jump_url 
        )

        embed.set_author(
            name=f"{after.author.display_name} ({after.author.id})",
            icon_url=after.author.display_avatar.url
        )

        old_content = (before.content[:1021] + '...') if len(before.content) > 1024 else before.content
        new_content = (after.content[:1021] + '...') if len(after.content) > 1024 else after.content

        embed.add_field(name="Before", value=old_content or "*[No text]*", inline=False)
        embed.add_field(name="After", value=new_content or "*[No text]*", inline=False)
        embed.add_field(name="Channel", value=after.channel.mention, inline=False)

        logs = self.bot.get_channel(log_channel)
        if logs:
            await logs.send(embed=embed)


async def setup(bot):
    await bot.add_cog(SniperCog(bot))