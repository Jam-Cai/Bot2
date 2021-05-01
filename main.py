import asyncio
import logging
import random
import os
import discord
from discord.utils import get
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('NTgxMjk1MjYwMTE4ODEwNjQy.XOdLZQ.EncOJW0jk-ccCx4G-F_fC8ur61g'))