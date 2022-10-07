# discord.py-bot
Discord.py bot public repo for the "make a bot for discord with python" series
## Lesson 1
Added bot.py code to create a discord.py bot, and a ping command.
Replace "your token here" to [your bot token](https://discord.com/developers/applications)

## Lesson 2
Securize the bot and repos by adding an environment variable.
This way we're not uploading tokens to the public repo and everyone

**Windows powershell**
```powershell
    $env:token = "token"
```
**Linux bash**
```bash
    export token="token"
```