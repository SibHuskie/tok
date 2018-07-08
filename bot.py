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
default_invite = 'https://discord.gg/5hXms6M'
member_role = '465479590056296449'
owner_role = '465479184043606036'
manager_role = '465479196102230027'
admin_role = '465479205963038731'
mod_role = '465479218269257729'
punished_role = '465479862166224896'
release_date = '9th of July, 2018'
banner = 'https://gph.is/2NfJtGd'

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Saviors™'))
    
#                                                           EMOTES

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

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif"]

punchlinks = ["https://i.imgur.com/T2HdIv8.gif",
              "https://i.imgur.com/LZz65rg.gif",
              "https://i.imgur.com/FqPBIf3.gif",
              "https://i.imgur.com/KmqPDQG.gif",
              "https://i.imgur.com/yEx4aKu.gif"]

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

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
        msg.add_field(name=":handshake: Interactions", value="<@{}> licked <@{}>! I'm not sure what to think of this, you weirdos.".format(author.id, user.id))
    await client.say(embed=msg)
    
# ~hug <user>
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
    
# ~kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to kiss.")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":handshake: Interactions", value="<@{}> got a kiss from <@{}>! owo what's this?".format(user.id, author.id))
    await client.say(embed=msg)

# ~cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":handshake: Interactions", value="<@{}> is crying! Poor thing...".format(author.id))
    await client.say(embed=msg)
    
# ~punch <user>
@client.command(pass_context=True)
async def punch(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to punch.")
    else:
        msg.set_image(url="{}".format(random.choice(punchlinks)))
        msg.add_field(name=":handshake: Interactions", value="<@{}> got punched by <@{}>! Wow, calm down.".format(user.id, author.id))
    await client.say(embed=msg)
    
# ~spank <user>
@client.command(pass_context=True)
async def spank(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to spank.")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":handshake: Interactions", value="<@{}> got spanked by <@{}>! Get a room ...".format(user.id, author.id))
    await client.say(embed=msg)
    
# ~cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to cuddle.")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":handshake: Interactions", value="<@{}> cuddled <@{}>! Aww.".format(author.id, user.id))
    await client.say(embed=msg)
    
#                                                       EVERYONE
    
# ~suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    channel = client.get_channel('463857809138778113')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give a suggestion.\nExample: `~suggest Create a role called 'Weeb'.`.")
    else:
        if len(str(args)) > 500:
            msg.add_field(name=error_img, value="The suggestion cannot be longer than 500 characters.")
        else:
            m = discord.Embed(colour=0x84b5ed, description= "")
            m.title = ""
            m.set_footer(text=footer_text)
            m.add_field(name=":speech_balloon: ", value="{}".format(args))
            m.add_field(name="===============", value="Suggested by: `{}` ### `{}`\nIf you like this suggestion, react with :white_check_mark: and if you don't like it, react with :x:.".format(author, author.id))
            await client.send_message(channel, embed=m)
            async for message in client.logs_from(channel):
                if len(message.reactions) == 0:
                    await client.add_reaction(message, '\u2705')
                    await client.add_reaction(message, '\u274C')
                    break
                else:
                    print("")
            msg.add_field(name=":speech_balloon: ", value="Suggestion sent!\nYou can see it in <#463857809138778113>.")
    await client.say(embed=msg)
    
# ~invite
@client.command(pass_context=True)
async def invite(ctx):
    msg = discord.Embed(colour=0x84b5ed, url=default_invite, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":link: ", value="Here is the default server invite:\n{}".format(default_invite))
    await client.say(embed=msg)
    
# ~userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    punish = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=error_img, value="Please tag the user you want to get information on.")
    else:
        imageurl = userName.avatar_url
        msg.title = ":page_with_curl: USER INFORMATION"
        msg.set_thumbnail(url=imageurl)
        msg.add_field(name="NAME:", value="`{}`".format(userName), inline=True)
        msg.add_field(name="ID:", value="`{}`".format(userName.id), inline=True)
        msg.add_field(name="CREATED AT:", value="`{}`".format(userName.created_at), inline=True)
        msg.add_field(name="JOINED AT:", value="`{}`".format(userName.joined_at), inline=True)
        msg.add_field(name="STATUS:", value="`{}`".format(userName.status), inline=True)
        msg.add_field(name="IS BOT:", value="`{}`".format(userName.bot), inline=True)
        msg.add_field(name="GAME:", value="{}".format(userName.game), inline=True)
        msg.add_field(name="NICKNAME:", value="`{}`".format(userName.nick), inline=True)
        msg.add_field(name="TOP ROLE:", value="`{}`".format(userName.top_role), inline=True)
        msg.add_field(name="VOICE CHANNEL:", value="`{}`".format(userName.voice_channel), inline=True)
        if punish in userName.roles:
            msg.add_field(name="PUNISHED:", value="True", inline=True)
        else:
            msg.add_field(name="PUNISHED:", value="False", inline=True)
    await client.say(embed=msg)
    
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.set_footer(text=footer_text)
    imageurl = ctx.message.server.icon_url
    msg.set_thumbnail(url=imageurl)
    msg.add_field(name="MEMBERS", value="`{}`".format(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value="`{}`".format(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value="`{}`".format(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value="`{}`".format(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value="`{}`".format(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value="`{}`".format(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value="`{}`".format(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value="`{}`".format(ctx.message.server.created_at), inline=True)
    msg.add_field(name="RELEASE DATE:", value="`{}`".format(release_date), inline=True)
    msg.set_image(url="{}".format(banner))
    await client.say(embed=msg)
    
#                                                       FUN

# ~kill <user>
@client.command(pass_context=True)
async def kill(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention the user you want to kill.")
    else:
        msgs = ["On a beautiful, sunny day, <@{}> went to the store. As they walked in to the store, they slipped and the doors cut off their head.".format(user.id),
                "<@{}> was sitting on a tree, but because of their weight, the branch broke and they fell right on their head.".format(user.id),
                "On a beautiful morning <@{}> suddenly jumped out of bed and started running towards the bathroom. However, they slipped on a banana and fell out of the window.".format(user.id),
                "<@{}> watched the Emoji movie. The next day they died from too much cringe.".format(user.id),
                "<@{}> was browsing the web one day. They accidentaly clicked on a pop-up saying 'DIE FOR FREE!'.".format(user.id),
                "<@{}> got caught watching hentai. They had no choice but to kill themselves in order to wash away their sins.".format(user.id),
                "All of <@{}>'s memes got stolen! They couldn't live for more than 0.420 seconds without memes.".format(user.id),
                "<@{}> was walking down the village when all of a sudden a piano fell on top of them, crashing all their bones.".format(user.id),
                "Long time ago <@{}> lived in peace and harmony, until the fire nation attacked. Now <@{}> is pretty much dead.".format(user.id, user.id),
                "<@{}> died a virgin. LMAO what a loser.".format(user.id),
                "<@{}> was playing hopscotch on a landmine field. You can tell how that went.".format(user.id),
                "<@{}> was playing the Sims. Their computer crashed and they got a heart attack.".format(user.id),
                "Wait, <@{}> died? Oh well.".format(user.id),
                "<@{}> commited suicide. I guess it's a way of saying 'You can't fire me! I quit!' to God.".format(user.id),
                "<@{}> gave their heart to <@{}>... Literally.".format(user.id, author.id),
                "There hasn't been rain around the whole world, plants are dying and the temperatures are very high. <@{}> was a vegan.".format(user.id),
                "<@{}> decided to go on the moon. However they forgot their space suit. All the kids wanted to hear about the corpse on the moon...".format(user.id),
                "One day <@{}> was chilling with their friends. All of them were bored, they didn't have anything to do. One of them said 'So gentlemen, what do we do now?', <@{}> replied: 'We die.'. Yeah, they were really bored.".format(user.id, user.id),
                "<@{}> tried to lay an egg. Humans can't do that, nor can bots!".format(user.id),
                "All of <@{}>'s diamonds were stolen on their Christian minecraft server. Out of anger they said 'heck' and got killed instantly.".format(user.id),
                "<@{}> forgot how to breathe.".format(user.id),
                "<@{}> saw <@{}>'s face and instantly died.".format(user.id, author.id),
                "...and then <@{}> said: I don't feel so good...".format(user.id),
                "<@{}> livedn't.".format(user.id),
                "<@{}> had a lot of mental disorders and couldn't live with them anymore. They commited suicide by cutting a deep wound on their chest with a kitchen knife.".format(user.id),
                "<@{}> drowned <@{}> in a glass of water.".format(author.id, user.id),
                "<@{}> threw <@{}> in a pool with sharks.".format(author.id, user.id),
                "<@{}> spammed <@{}>'s DMs and they died from all the notifications they got.".format(author.id, user.id),
                "<@{}> stole all of <@{}>'s chocolate. <@{}> simply couldn't live without their chocolate and decided that their life is not worth living anymore.".format(author.id, user.id, user.id),
                "<@{}>'s toaster was hacked by <@{}>. They couldn't live with no toast.".format(user.id, author.id),
                "<@{}> watched furry porn and died from what they saw.".format(user.id),
                "<@{}> 'accidentally' fell off a building.".format(user.id),
                "<@{}> may have ate food with cyanide.".format(user.id),
                "<@{}> starved in a fast food restaurant. What a fucking idiot.".format(user.id),
                "...And <@{}> died happily ever after... Wait no, I messed it up!".format(user.id),
                "<@{}> joined this server and died. Oh well, that's not a first.".format(user.id),
                "<@{}> was gay in Iran.".format(user.id),
                "<@{}> choked on a banana ( ͡° ͜ʖ ͡°) and died.".format(user.id),
                "<@{}> drove off a cliff and survived, but died from shock when they saw the high price of the hospital bill.".format(user.id),
                "<@{}> listened to Justin Beiber for more than 0.69 seconds.".format(user.id),
                "<@{}> drank too much anti-freeze.".format(user.id),
                "<@{}> got stabbed with a cucumber by <@{}>.".format(user.id, author.id),
                "<@{}> died from a heatstroke in the artic.".format(user.id),
                "<@{}> tried to fly. It worked till they hit the ground.".format(user.id),
                "<@{}> wanted to get a haircut in a faster way. They thought setting their hair on fire would do the trick.".format(user.id),
                "On a peaceful night. The moon was shining and everyone was sleeping and enjoying their dreams while <@{}> suffocated in their pillow.".format(user.id),
                "<@{}> got run over by a boat. A fricking boat!".format(user.id),
                "What's that smell? It smells like toast... Hey, <@{}>! Don't take out the toast with a fork- too late...".format(user.id),
                "<@{}> got a paper cut on both of their eyes, walked off a cliff and died. I guess books are evil.".format(user.id),
                "<@{}> tried putting out fire with gasoline.".format(user.id),
                "<@{}>'s head exploded while they were sitting on the toilet and pressing.".format(user.id),
                "<@{}> died of laughter. No I mean they actually died.".format(user.id),
                "<@{}> got locked in a refrigerator and died of hunger.".format(user.id),
                "<@{}> drowned in their own tears after losing a game of Fortnite.".format(user.id),
                "<@{}> got beat up by their imaginary friends.".format(user.id),
                "<@{}> played My Little Ponny for too long.".format(user.id),
                "<@{}> choked on air.".format(user.id),
                "<@{}> got poked by Chuck Norris.".format(user.id),
                "<@{}> took a selfie with a gun.".format(user.id),
                "<@{}>'s brain exploded after <@{}> saying 'What if dolphins had legs?'.".format(user.id, author.id),
                "<@{}> died after eating their favourite snack, tide pods.".format(user.id),
                "<@{}> survived the biggest waves then tripped on a rock and died.".format(user.id),
                "<@{}> ate white chocolate. Who the fuck eats white chocolate?".format(user.id),
                "<@{}> demonstrated how to die and then had a heart attack. How ironic.".format(user.id),
                "<@{}> fell in a toilet and then got flushed.".format(user.id),
                "<@{}> got stuck in a vending machine.".format(user.id),
                "<@{}> choked on their toothbrush and died.".format(user.id),
                "<@{}> found their butthole and died from excitement.".format(user.id),
                "<@{}> died. That's it. They just died.".format(user.id)]
        msg.add_field(name=":newspaper2: ", value="{}".format(random.choice(msgs)))
    await client.say(embed=msg)
    
# ~eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please ask a yes/no question.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The question cannot be longer than 1900 characters.")
        else:
            a = ["Hell no!",
                 "No!",
                 "Hell yes!",
                 "Yes!",
                 "Definitely!",
                 "Definitely not!",
                 "Probably!",
                 "Probably not!",
                 "Most likely!",
                 "Yes! I'm sure of it!",
                 "No! I'm sure of it!"]
            msg.add_field(name=":8ball: ", value=":grey_question: `Question:`\n<@{}>: {}\n \n:grey_exclamation: `Answer:`\n**Magic Eight Ball**: {}".format(author.id, args, random.choice(a)))
    await client.say(embed=msg)
    
# `rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Nothing to rate given.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The text cannot be longer than 1900 characters.")
        else:
            msg.add_field(name=":scales:", value=":arrow_forward: <@{}>\nI'd rate {} a {}/10!".format(author.id, args, random.randint(0, 11)))
    await client.say(embed=msg)
    
# ~dicklength
@client.command(pass_context=True)
async def dicklength(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    choice = random.randint(0, 10)
    if choice == 0 or choice == 1:
        c = random.randint(0, 1)
        if c == 1:
            msg.add_field(name=":straight_ruler: ", value="I'm sorry, <@{}>, your dick ran away.".format(author.id))
        else:
            msg.add_field(name=":straight_ruler: ", value="I'm sorry, <@{}>, your dick fell off.".format(author.id))
    elif choice == 9 or choice == 10:
        msg.add_field(name=":straight_ruler: ", value="Currently <@{}>'s dick is too big for me to take the length of it.".format(author.id))
    else:
        msg.add_field(name=":straight_ruler: ", value="Currently, <@{}>'s dick is {}cm long.".format(author.id, random.randint(1, 101)))
    await client.say(embed=msg)
    
# ~urban <text>
@client.command(pass_context=True)
async def urban(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give something you want to define.")
    else:
        if len(str(args)) > 150:
            msg.add_field(name=error_img, value="The text cannot be longer than 150 characters.")
        else:
            try:
                defs = ud.define('{}'.format(args))
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \n{}".format(author.id, args, random.choice(defs)))
            except:
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \nNo definition found.".format(author.id))
    await client.say(embed=msg)

client.run(os.environ['BOT_TOKEN'])
