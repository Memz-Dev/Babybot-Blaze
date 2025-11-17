import discord
from discord.ext import commands
from utils.helpers import *

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        setAllowedGuilds(self,{1347246964865105972})

    @commands.command()
    async def listcommands(self, ctx, member: discord.Member = None):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        
        await ctx.send("!slopmeplease\n!album\n!trello")

    @commands.command()
    async def album(self, ctx):
        
        result = get_release(get_music_id())
        
        embed = discord.Embed(
                    title=f"Current Album: {result['artists'][0]['name']} - {result['title']}",
                    description=f"Year: {result['year']}\nGenre: {', '.join(result['genres'])}\nStyles: {', '.join(result['styles'])}",
                    color=0x00FF00
                )
        embed.set_thumbnail(url=result['images'][0]['uri'])
        embed.add_field(name="Notes", value=get_music_description(), inline=False)
        embed.add_field(name="Tracklist", value="\n".join([f"{track['position']}. {track['title']} ({track['duration']})" for track in result['tracklist']]), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def setalbum(self, ctx, releaseID: int, *, description: str = "No description provided"):
        if ctx.author.id != 524292628171325442:
            await ctx.send("stupid bitch member")
            return
        result = get_release(releaseID)
        set_music(releaseID, description)
        await ctx.send(f"Album set to: {result['artists'][0]['name']} - {result['title']}")

    @commands.command()
    async def channelOrder(self, ctx):
        if ctx.author.id != 524292628171325442:
            await ctx.send("stupid bitch member")
            return

        channels = ctx.guild.channels
        chan_list = "\n".join([f"{ch.name} ({ch.id})" for ch in channels])
        await ctx.send(f"waoww here all channel:\n{chan_list}")

    @commands.command()
    async def trello(self,ctx):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        await ctx.send("https://trello.com/b/fF4kEIqI/crash-out-shit")



async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
