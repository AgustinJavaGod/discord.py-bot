import random
from discord.ext import commands

# Lista de palabras
palabras = ['Hola', 'Adiós', 'Python', 'Discord', 'PyCord']

class Randomword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command random message loaded")

    @commands.command(
        name='randomword',
        description='Receive a random word with a mention'
    )
    async def randomword(self, ctx):
        user = ctx.author.mention
        randomword = random.choice(palabras)
        await ctx.send(f'{user}, aquí tienes una palabra aleatoria: {randomword}')

def setup(bot):
    bot.add_cog(Randomword(bot))