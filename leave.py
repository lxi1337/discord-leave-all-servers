import discord
from discord.ext import commands, tasks





client = discord.Client()   
client= commands.Bot(command_prefix=">", self_bot=True)
client.remove_command("help")
token = input("Token > ")






@client.event
async def on_connect():
    for guild in client.guilds:
        try: 
             await guild.leave()
        except:
            await guild.delete()
            

client.run(token, reconnect=True, bot=False)
