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
                "crashout": "shut mouth",
                "rofighters": "26 years",
                "anna" : "honest low tier",
                "latinx" : "<@852600131932651551>",

                "w reza":"https://cdn.discordapp.com/attachments/1266031817602109563/1420160193676841091/99E83BBA-0FD3-42EB-BC94-794CA8DC24A1-ezgif.com-video-to-gif-converter.gif?ex=69179f3f&is=69164dbf&hm=b7154e51cba7a616c56e3121710e9f13714df7c130b43992ad4418f1a35e3a2d&",
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
