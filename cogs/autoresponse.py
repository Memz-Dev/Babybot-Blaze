import discord
import re
from discord.ext import commands
from utils.helpers import *

class ResponseCog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot

        setAllowedGuilds(self,{1347246964865105972,1415255360473796692})

        self.responses = {
                "kazuya": "sigma",
                "asuka": "stupid bitch character",
                "crashout": "shut mouth",
                "rofighters": "26 years",
                "anna" : "honest low tier",
                "latinx" : "<@852600131932651551>",
                "skylar" : "#1 consent hater 🔥",
                "hawk tuah" : "<@954253664585924628>",
                "joshy" : "lowslop grabslop",
                "w reza":"https://cdn.discordapp.com/attachments/1266031817602109563/1420160193676841091/99E83BBA-0FD3-42EB-BC94-794CA8DC24A1-ezgif.com-video-to-gif-converter.gif?ex=69179f3f&is=69164dbf&hm=b7154e51cba7a616c56e3121710e9f13714df7c130b43992ad4418f1a35e3a2d&",
                "ms2k" : "https://tenor.com/view/martinsugar2k-gif-5932750616034456338",
                "kunimitsu" : "https://tenor.com/view/low-parry-low-parry-tekken-7-gif-2181756876575504452",
                "release" : "kys",
                "chud" : "https://cdn.discordapp.com/attachments/1348640981586808882/1454964167420411954/images.png?ex=69530079&is=6951aef9&hm=7c381e931e19eb9875f7ad659c40f56521d8edea9f43990ab50c1a4b7f4bbfc9&",
                "guilty gear" : "BANNED WORD",
                "ggst" : "BANNED WORD",
                "origin" : "Do you believe in the big bang theory or pangrea?",
                "king" : "Well I guess just try to break his grabs everytime he tries to grab, and if he should ever whiff then get a combo on him",
                "sloppy" : "https://tenor.com/view/ltg-low-tier-god-lowtiergod-pizza-hut-your-mom-gif-13525585162005217098",
                "bryan" : "just sidestep right bro",
                "jin" : "realest mishima",
                "unc still got it" : "https://tenor.com/view/unc-still-got-it-gif-6384030002593541773",
                "carried" : "https://media.discordapp.net/attachments/167635765008924672/1227386687173427241/ggs.gif?ex=692d6fad&is=692c1e2d&hm=584d78b35178c438e3bd12052968fd7b2587074b3eefcdc9b89272e506a847c3&",
                "tmm" : "https://cdn.discordapp.com/attachments/1348639986399969332/1444114558292725810/tuffy.gif?ex=692b87fd&is=692a367d&hm=306401526394d93bf804ce2cb084e6aed803fbf971c88becde045c51267ea042&",
                "mainman" : "https://cdn.discordapp.com/attachments/1348639986399969332/1444114558292725810/tuffy.gif?ex=692b87fd&is=692a367d&hm=306401526394d93bf804ce2cb084e6aed803fbf971c88becde045c51267ea042&",
                "paul" : "https://tenor.com/view/fuzzydimonds-fuzzmanse-paul-pheonix-tekken-tag-tournament-2-tt2-gif-6154751673589864114",
                "revelation" : "https://tenor.com/view/rampage-rampage-dance-roblox-2025-martinsugar2k-gif-17940715652268577462",
                "stfu" : "https://cdn.discordapp.com/attachments/982073899300814888/1328158913568440361/Gagamaru.gif?ex=691720a0&is=6915cf20&hm=c70a9108e26f6a4a43d8ed28cf9557c6f7b8975bd898fa6844609c4889ff8408&",
                "connection" : "https://tenor.com/view/patrick-crank-dat-gif-19328104",
                "desync" : "https://media.discordapp.net/attachments/1205017287111872544/1297959047558856765/speed.gif?ex=6917580f&is=6916068f&hm=1bd3bef536e7684ef7d722f76e485f2630bf847378a0961da105f208b7cf5b57&",
            }
        
        
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not isAllowedInGuild(self,message.guild.id): 
            return
        
        # ignore messages from bots
        if message.author.bot:
            return
        
        if message.channel.id == auto_slop_channel:

            role = message.guild.get_role(slopperRole)
            await message.author.add_roles(role)
            add_to_list(message.author.id)

            await message.delete()

            return

        # lowercase content for case-insensitive matching
        msg_content = message.content.lower()

        for phrase, reply in self.responses.items():
            pattern = rf"\b{re.escape(phrase)}\b"

            if re.search(pattern, msg_content, flags=re.IGNORECASE):
                await message.reply(reply, mention_author=False)
                break

    @commands.command()
    async def wordlist(self,ctx):
        if not await author_is_owner(ctx):
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
