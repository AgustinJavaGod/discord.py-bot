from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command ping loaded")

    @commands.slash_command(
        name='ping',
        description="Ping command"
    )
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'pong 🏓! {latency}ms.')

def setup(bot):
    bot.add_cog(Ping(bot))