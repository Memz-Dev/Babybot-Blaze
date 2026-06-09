import json
import os
import discord
import requests
import aiohttp

# ----- Config -----
slopperRole = 1348641007948005416  # role ID for slop
purgatory = 1348640981586808882
auto_slop_channel = 1348640858169282614
logs = 1348644498904977479
owner_id = 524292628171325442

REPO_API = "https://api.github.com/repos/memz-dev/babybot-blaze/branches/main"
BOT_PATH = "/home/memz/Babybot-Blaze"
UPDATE_SCRIPT = f"sudo {BOT_PATH}/update_bot.sh"
RESTART_SCRIPT = f"sudo {BOT_PATH}/restart.sh"
VERSION_FILE = f"{BOT_PATH}/.version"

DATA_FILE = "members.json"
MUSIC_FILE = "music.json"
SKYLAR_FILE = "skylarfiles.json"
SKYLAR_BOTS = "skylarbots.json"

NO_PERMISSIONS = "stupid bitch admin give perms"
ERROR_MESSAGE = "stupid error msg"

# ----- Persistent storage -----
if os.path.exists(SKYLAR_FILE):
    with open(SKYLAR_FILE, "r") as f:
        skylarFiles = json.load(f)
else:
    skylarFiles = []

if os.path.exists(SKYLAR_BOTS):
    with open(SKYLAR_BOTS, "r") as f:
        skylarBots = json.load(f)
else:
    skylarBots = {}

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


# ------- Version fetching --------
def get_local_version():
    with open(".version") as f:
        version = f.read().strip()
    return version
    
def get_remote_version():
    resp = requests.get(REPO_API)
    resp.raise_for_status()
    data = resp.json()
    return data["commit"]["sha"][:7]
# ---------------------------------

def setAllowedGuilds(cog,listOfGuilds):
      cog.allowList = listOfGuilds

def isAllowedInGuild(cog,serverID):
      return serverID in cog.allowList

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(stored_members, f, indent=4)

# ----- Permissions -----
def has_manage_roles(ctx):
    return ctx.author.guild_permissions.manage_roles

async def author_is_owner(ctx):
      if ctx.author.id != 524292628171325442:
            await ctx.send("stupid bitch member")
            return False
      return True

async def quick_check_roleEdit(ctx):

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

async def announce_slopped_member(bot,member,reason):
    channel = bot.get_channel(purgatory)
    log_channel = bot.get_channel(logs)

    await log_channel.send(f"<@{member.id}> entered purgatory: {reason}")

    await channel.send(f"welcome to purgatory <@{member.id}>\n{reason}")


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


    
