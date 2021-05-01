import asyncio
import logging
import random
import os
import discord
from discord.utils import get
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello dumbass!')
    await bot.process_commands(message)
@bot.command(help = "Adds new event to database")
async def add_event(ctx):
    messages = ["Event Name: ", "Date in form of DD/MM/YYYY: ", "Time of Day", "Details of event: "]
    keys = ['name', 'day', 'time', 'details']
    eventData = {}
    
    for i in range(4):
        await ctx.send((messages[i]))
        try:
            dataName = await bot.wait_for('message', timeout=60)
            eventData[keys[i]] = dataName.content
        except asyncio.TimeoutError:
            ctx.send("Timed Out")

    data = {}
    data[eventData['name']] = eventData
    with open("Events.json", "r+") as f:
        jsonData = json.load(f)
        jsonData["events"].update(data)
        f.seek(0)
        json.dump(jsonData, f, indent=4)


@bot.command(help = "Reads all events")
async def read_events(ctx,arg = None):
    with open("Events.json", "r+") as f:
        jsonData = json.load(f)
    print(jsonData["events"])
    jsonKeys = list(jsonData["events"].keys())
    jsonKeys.sort()
    print(jsonKeys)
    for key in jsonKeys:
        output = ""        
        for attribute in ['name', 'day', 'time', 'details']:
            output += jsonData["events"][key][attribute]
            output += "\n"
        output += "\n"
        await ctx.send(output)

    

with open("Token.txt") as t:
    bot.run(t.readline().rstrip())