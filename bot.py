import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix='$', description="AgustinJavaGod bot",intents=discord.Intents.all())
token = os.getenv("token")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="videos explained even better than I explain"))
    print("Ready")

from commands.ping import Ping

bot.add_cog(Ping(bot))
bot.remove_command("help")

bot.run(token)