import discord, random
from discord.utils import get
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:return
    role = discord.utils.get(message.guild.roles, id=991009276946419714)
    if not role in message.author.roles:return
    words=["素晴らしい", "素晴らしいな", "素晴らしい:clap:", "素晴らしいな:clap:"]
    if ("素晴らしいな") in message.content:    
        await message.channel.send(random.choice(words))
    elif ("素晴らしい") in message.content:
        await message.channel.send(random.choice(words))
    elif ("👏") in message.content:
        await message.channel.send(random.choice(words))
    elif ("すばらしい") in message.content:
        await message.channel.send(random.choice(words))

client.run()   
