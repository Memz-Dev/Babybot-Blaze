import asyncio
import discord
from discord.ext import commands
from utils.helpers import *
import random

async def get_release_async(id):
    url = f"https://api.discogs.com/releases/{id}"
    headers = {
        "User-Agent": "BabyBotBlaze/1.0"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status != 200:
                return f"Error fetching release: {resp.status}"
            return await resp.json()

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def album(self, ctx):
        
        result = await get_release_async(get_music_id())
        
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
        if not await author_is_owner(ctx):
            return
        result = await get_release_async(releaseID)
        set_music(releaseID, description)
        await ctx.send(f"Album set to: {result['artists'][0]['name']} - {result['title']}")

async def setup(bot):
    await bot.add_cog(MusicCog(bot))
