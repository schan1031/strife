import os
import discord
import time
from dotenv import load_dotenv
from session import Session
from pprint import pprint

load_dotenv()
client = discord.Client()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

class DiscordHandler(discord.Client):

    def __init__(self):
        self.client = discord.Client()

        return

    def handle_reaction(self):
        print('handle')
        
        return

live_sessions = {}

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!newgame':
        board = discord.Embed(description='This is a new game.')
        board.add_field(name='Enemy', value='Goblin')
        board.set_footer(text='Options')

        message = await message.channel.send(embed=board)
        choices = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
        
        for reaction in choices:
            await message.add_reaction(reaction)


    if message.content.startswith('$hello'):
        msg = await message.channel.send('Hello!')

        await msg.add_reaction('👍')

    
    if message.content.startswith('!addcount'):
        pprint(message)
        session = live_sessions.get(message.author.id, None)
        if not session:
            session = Session(message.author.id)
            live_sessions[message.author.id] = session

            print('New session')
            await message.channel.send('new session')
        else:
            print('Found session')
            await message.channel.send('found session')

client.run(DISCORD_TOKEN)