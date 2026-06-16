import asyncio
import discord
from discord.ext import commands
from utils.helpers import *
import random

emojis = ['🫃', '💀', '🥀']

async def slime_message(message):
        for emoji in emojis:
                try:
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
    async def skylaraccounts(self, ctx):
        
        embed = discord.Embed(
                    title=f"Skylar's AI Accounts",
                    description=f"",
                    color=0x00FF00
                )
        embed.add_field(name="Character AI", value=f"{skylarBots.get("character_ai_account").get("user")}\n[Link]({skylarBots.get("character_ai_account").get("link")})", inline=False)
        embed.add_field(name="Janitor AI", value=f"{skylarBots.get("janitor_ai_account").get("user")}\n[Link]({skylarBots.get("janitor_ai_account").get("link")})", inline=False)
        embed.add_field(name="Tiktok", value=f"{skylarBots.get("tiktok_account").get("user")}\n[Link]({skylarBots.get("tiktok_account").get("link")})", inline=False)
        embed.add_field(name="DeviantArt", value=f"{skylarBots.get("deviant_art_account").get("user")}\n[Link]({skylarBots.get("deviant_art_account").get("link")})", inline=False)
        embed.add_field(name="Reddit", value=f"{skylarBots.get("reddit_account").get("user")}\n[Link]({skylarBots.get("reddit_account").get("link")})", inline=False)
        embed.add_field(name="Twitter", value=f"{skylarBots.get("twitter_account").get("user")}\n[Link]({skylarBots.get("twitter_account").get("link")})", inline=False)
        embed.add_field(name="Twitch", value=f"{skylarBots.get("twitch_account").get("user")}\n[Link]({skylarBots.get("twitch_account").get("link")})", inline=False)
        embed.add_field(name="YouTube", value=f"{skylarBots.get("youtube_account").get("user")}\n[Link]({skylarBots.get("youtube_account").get("link")})", inline=False)

        await ctx.send(embed=embed)

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

    

    @commands.command()
    async def slime(self, ctx):
        if not await author_is_owner(ctx):
            return

        if ctx.message.reference:
            target_message = ctx.message.reference.resolved
            if not isinstance(target_message, discord.Message):
                try:
                    target_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
                except discord.NotFound:
                    await ctx.send("waoww! Cannot find message you replied to!")
                    return

            await slime_message(target_message)            
        else:
            await ctx.send("reply you bum")

    @commands.command()
    async def skylargooned(self, ctx):
        char_list = skylarFiles.get("characters", [])
        
        if char_list:
            chosen_char = random.choice(char_list)
            await ctx.send(f"skylar has gooned to {chosen_char}")


    @commands.command()
    async def skylarquote(self,ctx):
        await ctx.send(f"skylar: '{skylarFiles.get("caption")}'")

    @commands.command()
    async def goonlist(self,ctx):
        await ctx.send(f"[skylar goon list](https://github.com/Memz-Dev/Babybot-Blaze/blob/main/skylarfiles.json)")

    @commands.command(aliases=['pu'])
    async def purgeuser(self,ctx, member: discord.Member = None,amount = 1):
        if not await author_is_owner(ctx):
            return
        
        totalPurged = 0
        
        for channel in ctx.guild.text_channels:
            deleted = 0
            try:
                def is_target(msg):
                    if (msg.author.id == member.id) and deleted<amount:
                        deleted += 1
                        totalPurged+=1
                        return True
                    else:
                        return False

                await channel.purge(limit=20, check=is_target)
            except:
                continue
        await ctx.reply(f"Purged {totalPurged} messages.")


async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
