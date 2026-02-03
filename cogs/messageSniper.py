import datetime
import discord
from discord.ext import commands
from utils.helpers import *

class SniperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})

    

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        if message.author.bot:
            return

        if not message.content and not message.attachments:
            return

        # 3. Create the "Caught" embed
        embed = discord.Embed(
            title="lil jit tryna delete",
            description=message.content if message.content else "*[No text content]*",
            color=0xff4747, # Bright red
            timestamp=datetime.datetime.now()
        )

        embed.set_author(
            name=f"{message.author.display_name} ({message.author.id})",
            icon_url=message.author.display_avatar.url
        )

        # 4. Handle images/attachments
        if message.attachments:
            # We try to grab the first image if it exists
            embed.set_image(url=message.attachments[0].url)
            embed.add_field(name="Attachments", value=f"{len(message.attachments)} file(s) attached")

        # 5. Send it immediately back to the channel where it was deleted
        await message.channel.send(content=f"**{message.author.mention}**", embed=embed)



async def setup(bot):
    await bot.add_cog(SniperCog(bot))
