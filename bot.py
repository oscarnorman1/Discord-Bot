# bot.py
import discord, json
from reddit import redditBot

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

            reddit_raw_data = redditBot(message.content.split('!')[1])
            reddit_data = json.loads(reddit_raw_data)

            response = '```'
            response += '**Title:**\n\n{}'.format(reddit_data['title'])
            response += '\nUptvotes: {}'.format(reddit_data['ups'])
            response += '\n\n---TOP COMMENTS---\n\n'
            response += '#1 Upvotes: {} | {}\n\n'.format(reddit_data['oneUps'], reddit_data['one'])
            response += '#2 Upvotes: {} | {}\n\n'.format(reddit_data['twoUps'], reddit_data['two'])
            response += '#3 Upvotes: {} | {}\n\n'.format(reddit_data['threeUps'], reddit_data['three'])
            response += '#4 Upvotes: {} | {}\n\n'.format(reddit_data['fourUps'], reddit_data['four'])
            response += '#5 Upvotes: {} | {}\n\n'.format(reddit_data['fiveUps'], reddit_data['five'])
            response += '```'
            
            await channel.send(response)

client.run(TOKEN)