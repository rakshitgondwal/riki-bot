import os
import discord
import requests
import json  
from keep_alive import keep_alive

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)

def getJoke():
  response = requests.get("https://hindi-jokes-api.onrender.com/jokes?api_key=339b8a63bc0ffb9a50b44afae844")
  
  json_data = json.loads(response.text)
  joke = json_data['jokeContent']
  return(joke)


@client.event
async def on_ready():
  print('Hey everyone! I am a bot created by Rakshit')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('armaan'):
    await message.channel.send('billo')

  haha = getJoke()
  
  if message.content.startswith('joke'):
    await message.channel.send(haha)

  if msg.startswith('reaction'):
    await message.channel.send(file=discord.File('armaan.png'))

  if msg.startswith('xzile'):
    await message.channel.send(file=discord.File('xzile.png'))


keep_alive()

client.run(os.getenv('CLIENT_ID'))
