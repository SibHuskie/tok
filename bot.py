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
footer_text = "Saviors™"
error_img = ':warning:'

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Saviors™'))
    
#EMOTES

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

# ~lick <user>
@client.command(pass_context=True)
async def lick(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to lick.")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name=":weary: __**Emotes**__ :weary:", value="<@{}> licked <@{}>! I'm not sure what to think of this, you weirdos.".format(author.id, user.id))
    await client.say(embed=msg)
    
# }hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to hug.")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":handshake: Interactions", value="<@{}> got a hug from <@{}>! How cute.".format(user.id, author.id))
    await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
