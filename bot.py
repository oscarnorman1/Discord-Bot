# bot.py
import os, discord, random, time, threading
from tracemalloc import start


TOKEN = 'MTAyMDQ0ODU5MTM1NTA2MDI3NA.Gl-Oao.JT_RjWIiN0Vdm7N_MJhrwBpQf4tt3QBZe3i5qA'
GUILD = '314124078657175553'

client = discord.Client(intents=discord.Intents.all())

threads = []

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
        'joppegay',
        'simpogay'
    ]

    if message.content == 'gay generator':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

@client.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel

    if after.channel is None: 
        print(member.name + " left")
        return

    if channel.id == 1021484776407957577 or channel.id == 767412462017576990 or channel.id == 688792120907137071:
        print(member.name + " joined")
        startThread(member.name)


def startThread(member):
        counter = memberSecondCounter()
        counter.name = member
        counter.start()
        threads.append(counter)

class memberSecondCounter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.alive = False
        self.start = time.time()

    def run(self):
        self.alive = True
        while self.alive:
            time.sleep(1)

    def finish(self):
        end = time.time()
        self.alive = False
        return self.start - end
        
        

for thread in threading.enumerate():
    print(thread.getName)

client.run(TOKEN)