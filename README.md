# discord.py-bot
Discord.py bot public repo for the "make a bot for discord with python" series

- [discord.py-bot](#discordpy-bot)
  - [Lesson 1](#lesson-1)
  - [Lesson 2](#lesson-2)
    - [**Windows powershell**](#windows-powershell)
    - [**Linux bash**](#linux-bash)
  - [Lesson 3](#lesson-3)
  - [Lesson 4](#lesson-4)

## Lesson 1
Added bot.py code to create a discord.py bot, and a ping command.
Replace "your token here" to [your bot token](https://discord.com/developers/applications)

## Lesson 2
Securize the bot and repos by adding an environment variable.
This way we're not uploading tokens to the public repo and everyone

### **Windows powershell**
```powershell
    $env:token = "token"
```
### **Linux bash**
```bash
    export token="token"
```

## Lesson 3
Making the project more secure by adding environment variables that each owner of this bot can use on his local machine.
This way there's no way of leaking secrets on public repos.

## Lesson 4
Making a modulable bot, using cogs for individual files for each command inside the folder commands.

## Lesson 5
Move the current bot from discord.py to py-cord to work with slash commands.