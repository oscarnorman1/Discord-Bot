# bot.py
import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'MTAyMDQ0ODU5MTM1NTA2MDI3NA.Gl-Oao.JT_RjWIiN0Vdm7N_MJhrwBpQf4tt3QBZe3i5qA'
GUILD = '1020449801730531370'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    print(message.content, "sent")
#    if message.author == client.user:
#        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)