import discord

TOKEN = 'bot_token_here'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    channelToSendTo = discord.utils.get(client.guilds[0].text_channels, name="replace_with_channel_name")

    if message.author.bot: #don't want bot to reply to itself
        return

    if isinstance(message.channel, discord.DMChannel): #message is a dm
        await channelToSendTo.send(message.content) #send the same message to the specified channel on line 9


@client.event
async def on_ready(): #ouput to the terminal when bot is ready
    for guild in client.guilds:
        print(client.user, 'connected to guild ', guild.name, '#', guild.id)

client.run(TOKEN)
