import discord, random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    words=["素晴らしい", "素晴らしいな", "素晴らしい:clap:", "素晴らしいな:clap:"]
    if message.content.endswith("素晴らしいな"):
        await message.channel.send(random.choice(words))
    elif message.content.endswith("素晴らしい"):
        await message.channel.send(random.choice(words))
    elif message.content.endswith("👏"):
        await message.channel.send(random.choice(words))
    if message.content.endswith("すばらしい"):
        await message.channel.send(random.choice(words))

client.run("TOKEN")
