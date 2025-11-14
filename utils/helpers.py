import json
import os
import discord

# ----- Config -----
slopperRole = 1348641007948005416  # role ID for slop
DATA_FILE = "members.json"

NO_PERMISSIONS = "stupid bitch admin give perms"
ERROR_MESSAGE = "stupid error msg"
# ----- Persistent storage -----
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_members = json.load(f)
else:
    stored_members = []

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
            return True
      return False

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
     
def add_to_list(id):
     if id not in stored_members:
                stored_members.append(id)
                save_data()

def remove_from_list(id):
     if id in stored_members:
                stored_members.remove(id)
                save_data()

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
    
