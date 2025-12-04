import asyncio
import discord
from discord.ext import commands
from utils.helpers import *

async def slime_message(message):
        for emoji in emojis:
                try:
                    # Add the reaction to the target message
                    await message.add_reaction(emoji)
                except Exception as e:
                    print(f"Error adding reaction {emoji}: {e}")

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
        if not await author_is_owner(ctx):
            return
        result = get_release(releaseID)
        set_music(releaseID, description)
        await ctx.send(f"Album set to: {result['artists'][0]['name']} - {result['title']}")

    @commands.command()
    async def channelOrder(self, ctx):
        if not await author_is_owner(ctx):
            return

        channels = ctx.guild.channels
        chan_list = "\n".join([f"{ch.name} ({ch.id})" for ch in channels])
        await ctx.send(f"waoww here all channel:\n{chan_list}")

    @commands.command()
    async def trello(self,ctx):
        if not isAllowedInGuild(self,ctx.guild.id): 
            return
        await ctx.send("https://trello.com/b/fF4kEIqI/crash-out-shit")

    @commands.command()
    async def purge(self, ctx, amount: int):
        if not (await ctx.author.guild_permissions.manage_messages or ctx.author.id == 524292628171325442):
            await ctx.reply("shut up bitch member")
            return

        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"deleted {amount} msg bruh")
        await asyncio.sleep(3)
        await msg.delete()

    

    emojis = ['🫃', '💀', '🥀']
    @commands.command()
    async def slime(self, ctx):
        global emojis
        await slime_message(ctx.message)
        # Check if the message is a reply to another message
        if ctx.message.reference:
            # Get the ID of the referenced message
            message_id = ctx.message.reference.message_id
            await ctx.send(message_id)
            
            # Get the actual message object that was replied to
            try:
                target_message = await ctx.fetch_message(message_id)
            except discord.NotFound:
                # If the replied message is not found (maybe it was deleted)
                await ctx.send("waoww! Cannot find message you replied to!")
                return
            
            await slime_message(target_message)
        else:
            # If the command was not a reply, tell the user!
            await ctx.send("You must reply to message with this command for it to work!")




async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
