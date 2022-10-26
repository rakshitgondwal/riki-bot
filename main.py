import os
import discord

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)


@client.event
async def on_ready():
  print('Hey everyone! I am a bot created by Rakshit')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$armaan'):
    await message.channel.send('Billo Rani')

botId = os.getenv('CLIENT_ID')

client.run(botId)
