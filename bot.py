import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os
import os.path
import requests
import json
import urbandictionary as ud

client = commands.Bot(command_prefix="~")
footer_text = "Saviours™"
error_img = ':warning:'

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Saviours™'))
client.run(os.environ['BOT_TOKEN'])
