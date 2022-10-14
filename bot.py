import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='$', description="AgustinJavaGod bot",intents=discord.Intents.all())
token = os.getenv("token")

load_dotenv()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="videos explained even better than I explain"))
    print(f"{bot.user.name} online")

async def load_extensions():
    for file in os.listdir("./commands"):
        if file.endswith('.py'):
            await bot.load_extension(f'commands.{file[:-3]}')

async def  main():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(main())
