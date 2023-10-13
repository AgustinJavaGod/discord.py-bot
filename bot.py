import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='$', description="AgustinJavaGod bot",intents=discord.Intents.all())
token = os.getenv("token")

load_dotenv()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="tengo el celular confiscado"))
    print(f"{bot.user.name} online")

async def load_extensions():
    for file in os.listdir("./commands"):
        if file.endswith('.py'):
            await bot.load_extension(f'commands.{file[:-3]}')
            print(f"{file[:-3]} está cargado!")

async def main():
    await load_extensions()
    await bot.start(token)

if __name__ == '__main__':
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[:-3]}')
    
bot.run(token)