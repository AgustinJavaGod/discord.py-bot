import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Bot {client.user} started')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('pong 🏓')

client.run('your token here')
