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
                "ms2k" : "https://tenor.com/view/martinsugar2k-gif-5932750616034456338",
                "kunimitsu" : "https://tenor.com/view/low-parry-low-parry-tekken-7-gif-2181756876575504452",
                "release" : "kys",
                "sloppy" : "https://tenor.com/view/ltg-low-tier-god-lowtiergod-pizza-hut-your-mom-gif-13525585162005217098",
                "bryan" : "just sidestep right bro",
                "jin" : "realest mishima",
                "stfu" : "https://cdn.discordapp.com/attachments/982073899300814888/1328158913568440361/Gagamaru.gif?ex=691720a0&is=6915cf20&hm=c70a9108e26f6a4a43d8ed28cf9557c6f7b8975bd898fa6844609c4889ff8408&",
                "connection" : "https://tenor.com/view/patrick-crank-dat-gif-19328104",
                "desync" : "https://media.discordapp.net/attachments/1205017287111872544/1297959047558856765/speed.gif?ex=6917580f&is=6916068f&hm=1bd3bef536e7684ef7d722f76e485f2630bf847378a0961da105f208b7cf5b57&",
            }
        
    @commands.Cog.listener()
    async def on_slop_message(self, message: discord.Message):
        if not isAllowedInGuild(self,message.guild.id): 
            return
        
        if message.channel.id != 1348640858169282614:
            return

        slop_member_from_message(message,message.author)
        
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

    @commands.command()
    async def wordlist(self,ctx):
        if not isOwner(ctx.author.id):
            return
        
        newString = ""

        for word,response in self.responses.items():
            newString += f"{word}\n"

        embed = discord.Embed(
                title="Trigger List",
                description=newString,
                color=0x00FF00
            )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ResponseCog(bot))
