import discord
from discord.ext import commands
from utils.helpers import *

class ResponseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})
        self.responses = {
                "kazuya": "sigma",
                "asuka": "stupid bitch character",
                "crashout": "shut mouth"
            }
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not isAllowedInGuild(self,message.guild.id): 
            return
        
        # ignore messages from bots
        if message.author.bot:
            return

        # lowercase content for case-insensitive matching
        msg_content = message.content.lower()

        for phrase, reply in self.responses.items():
            if phrase in msg_content:
                await message.reply(reply,mention_author=False)
                break  # respond only once per message


async def setup(bot):
    await bot.add_cog(ResponseCog(bot))
