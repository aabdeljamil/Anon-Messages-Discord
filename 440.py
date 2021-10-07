import discord

TOKEN = ''

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    id = #need channel id here
    channelToSendTo = client.get_channel(id)

    if message.author.bot:
        return

    if isinstance(message.channel, discord.DMChannel):
        await channelToSendTo.send(message.content)


@client.event
async def on_ready():
    for guild in client.guilds:
        print(client.user, 'connected to guild ', guild.name, '#', guild.id)

client.run(TOKEN)