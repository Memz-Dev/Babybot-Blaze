import json
import os
import discord
import requests

# ----- Config -----
slopperRole = 1348641007948005416  # role ID for slop
purgatory = 1348640981586808882
auto_slop_channel = 1348640858169282614

owner_id = 524292628171325442

DATA_FILE = "members.json"
MUSIC_FILE = "music.json"

NO_PERMISSIONS = "stupid bitch admin give perms"
ERROR_MESSAGE = "stupid error msg"
# ----- Persistent storage -----
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_members = json.load(f)
else:
    stored_members = []

if os.path.exists(MUSIC_FILE):
    with open(MUSIC_FILE, "r") as x:
        musicData = json.load(x)
else:
    musicData = {}

def setAllowedGuilds(cog,listOfGuilds):
      cog.allowList = listOfGuilds

def isAllowedInGuild(cog,serverID):
      return serverID in cog.allowList

def save_data():
    """Save the stored_members list to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(stored_members, f, indent=4)

# ----- Permissions -----
def has_manage_roles(ctx):
    """Check if the command author can manage roles"""
    return ctx.author.guild_permissions.manage_roles

async def author_is_owner(ctx):
      if ctx.author.id != 524292628171325442:
            await ctx.send("stupid bitch member")
            return False
      return True

async def quick_check_roleEdit(ctx):
    """Check if the command author can manage roles"""
    
    if not has_manage_roles(ctx):
        await ctx.send("shut up bitch member")
        return False

    return True

async def member_is_mentioned(member,ctx):
     if member is None:
            await ctx.send("u didnt @ someone retard")
            return False
     return True
     
def set_music(releaseID,description):
    musicData["id"] = releaseID
    musicData["description"] = description
    
    with open(MUSIC_FILE, "w") as x:
        json.dump(musicData, x, indent=4)
def get_music_description():
    return musicData.get("description", "No description provided")

def get_music_id():
    return musicData.get("id", None)

def get_list():
     return stored_members
    
def add_to_list(id):
     if id not in stored_members:
                stored_members.append(id)
                save_data()

def remove_from_list(id):
     if id in stored_members:
                stored_members.remove(id)
                save_data()

async def slop_member_from_message(message,member,ignore_write : bool = False):
    role = message.guild.get_role(slopperRole)

    await member.add_roles(role)
    add_to_list(member.id)
    return True

async def announce_slopped_member(bot,member):
    channel = bot.get_channel(purgatory)
    await channel.send(f"welcome to purgatory <@{member.id}>")


async def slop_member(ctx,member,ignore_write : bool = False):
    role = ctx.guild.get_role(slopperRole)

    try:
        await member.add_roles(role)
        if ignore_write == False:
              add_to_list(member.id)
        return True
    except discord.Forbidden:
            await ctx.send(NO_PERMISSIONS)
    except Exception as e:
            await ctx.send(f"{ERROR_MESSAGE}: {e}")  

async def unslop_member(ctx,member):
    role = ctx.guild.get_role(slopperRole)

    try:
        await member.remove_roles(role)
        remove_from_list(member.id)
        return True
    except discord.Forbidden:
            await ctx.send(NO_PERMISSIONS)
    except Exception as e:
            await ctx.send(f"{ERROR_MESSAGE}: {e}")  

def isOwner(memberID):
      return memberID == 524292628171325442

def get_release(id):
    url = f"https://api.discogs.com/releases/{id}"
    headers = {
        #"Authorization": f"Discogs token={DISCOGS_TOKEN}",
        "User-Agent": "BabyBotBlaze/1.0"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return f"Error fetching release: {resp.status_code}"
    return resp.json()
    
