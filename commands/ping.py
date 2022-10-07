from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name="ping",help="Answer pong",pass_context="True")
async def ping(self, ctx):
    await ctx.send('pong 🏓')