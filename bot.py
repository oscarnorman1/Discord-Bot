# bot.py
import discord, json
from reddit import redditBot
from table2ascii import table2ascii as t2a, PresetStyle

TOKEN = 'MTA0MzkxMjMzNDIwNjMxNjU5NQ.GO3C8F.AcZRbnoL5A69iIeFtRyVZFmAJ1sOxu5VwOy5HM'
CHANNEL_ID = '1021484821802930256'

intents = discord.Intents.default()
#intents.bot = True

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if (str(message.channel) == 'bot-test-text'):
        if (str(message.author) != str(client.user)):
            channel = client.get_channel(int(CHANNEL_ID))

            reddit_data = json.loads(redditBot(message.content.split('!')[1]))

            response = ''
            response += 'TITLE:\n{}'.format(reddit_data['title'])
            response += '\nUPVOTES: {}'.format(reddit_data['ups'])
            
            # In your command:
            output = t2a(
            header=["# Upvotes", "Comment"],
            body=[
            [reddit_data['top_comments'][0]['oneUps'], reddit_data['top_comments'][0]['one']], 
            [reddit_data['top_comments'][0]['twoUps'], reddit_data['top_comments'][0]['two']], 
            [reddit_data['top_comments'][0]['threeUps'], reddit_data['top_comments'][0]['three']],
            [reddit_data['top_comments'][0]['fourUps'], reddit_data['top_comments'][0]['four']],
            [reddit_data['top_comments'][0]['fiveUps'], reddit_data['top_comments'][0]['five']],
            ],
            style=PresetStyle.thin_compact
            )

            await channel.send(output)
            #await channel.send(response)
client.run(TOKEN)