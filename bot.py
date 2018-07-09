import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS
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
helper_role = '465675482654965762'
x_role = '465678190208090112'
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
    
# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    m2 = "https://gph.is/2NfJtGd"
    m2 += "\n**~~__= = = = = = = = = = = = = = = = = = =__~~**"
    m2 += "\n:small_red_triangle_down: Welcome to **Saviors™**, <@{}>! We hope you enjoy your stay and have fun.".format(userName.id)
    m2 += "\n:small_red_triangle:All the information is in the <#463180648719450112> channel, but feel free to ask the staff about anything you want to know."
    m2 += "\n**~~__= = = = = = = = = = = = = = = = = = =__~~**"
    m2 += "\n:small_orange_diamond: If you are here to partner with the server, please DM a Partnership Manager, if there are none online DM a helper / moderator instead of the managers and owners."
    m2 += "\n:small_blue_diamond: Thanks for joining!"
    server = client.get_server('463178197228584981')
    await client.send_message(client.get_channel("463178197228584983"), "Welcome to **Saviors™**, {}! We hope you enjoy your stay. We now have have {} members.".format(userName, len(server.members)))
    try:
        await client.send_message(userName, "{}".format(m2))
    except:
        print("")
        
@client.async_event
async def on_member_remove(userName: discord.User):
    server = client.get_server('463178197228584981')
    await client.send_message(client.get_channel("463178197228584983"), "`{}` left the server! Now we have {} members.".format(userName, len(server.members)))
    
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

punchlinks = ["http://www.reactiongifs.com/wp-content/uploads/2013/01/Superhero-Punch.gif",
              "http://78.media.tumblr.com/41ef6b8df3b90fcd28f9b4c0d0a72973/tumblr_mgle63eSBS1s31xf3o1_400.gif",
              "https://media.giphy.com/media/12eUd8OxABjQvS/giphy.gif"]

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
async def penislength(ctx):
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

#                                                       MODERATOR COMMANDS

# ~tempmute <user> <time> [reason]
@client.command(pass_context=True)
async def tempmute(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    member_role = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished_role = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=error_img, value="Not all required arguments were given.\nExamples:\n`~tempmute @Huskie 15 Spamming.`.\n`~tempmute @Huskie 15`.")
            await client.say(embed=msg)
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't punish other staff!`")
            await client.say(embed=msg)
        elif punished_role in userName.roles:
            msg.add_field(name=":warning: ", value="`That user is already muted!`")
            await client.say(embed=msg)
        else:
            time2 = time * 60
            if args == None:
                await client.add_roles(userName, punished_role)
                await client.remove_roles(userName, member_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been temporarily muted by {}! for {} minute(s)!`\n`Reason: ?`".format(userName.display_name, author.display_name, time))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
            else:
                await client.add_roles(userName, punished_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been muted by {} for {} minute(s)!`\n`Reason: {}`".format(userName.display_name, author.display_name, time, args))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
# ~unmute <user>
@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None):
    author = ctx.message.author
    member = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to unmute.\nExample: `~unmute @Huskie`.")
        else:
            if punished in user.roles:
                await client.remove_roles(user, punished)
                msg.add_field(name=":o: ", value="<@{}> pardoned <@{}>.".format(author.id, user.id))
            else:
                msg.add_field(name=error_img, value="That user isn't muted.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)
    
# ~bc
@client.command(pass_context=True)
async def bc(ctx):
    author = ctx.message.author
    chnl = ctx.message.channel
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    helper = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    a = []
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        async for i in client.logs_from(chnl):
            if len(a) < 50:
                if i.author.bot:
                    await client.delete_message(i)
                    a.append("+1")
                else:
                    print("")
            else:
                break
        msg.add_field(name="**Bot Clear**", value="<@{}> removed the latest messages sent by bots.".format(author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)
    
# ~purge <number>
@client.command(pass_context=True)
async def purge(ctx, number = None):
    author = ctx.message.author
    member = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if number == None:
            msg.add_field(name=error_img, value="Please specify the number of messages you want to delete.")
        else:
            try:
                testnumber = int(number)
                number2 = testnumber * 0
                await asyncio.sleep(float(number2))
                try:
                    deleted = await client.purge_from(ctx.message.channel, limit=testnumber)
                    if len(deleted) < testnumber:
                        msg.add_field(name=":wastebasket: ", value="<@{}> tried to delete {} messages.\n{} messages were deleted.".format(author.id, number, len(deleted)))
                    else:
                        msg.add_field(name=":wastebasket: ", value="<@{}> deleted {} messages.".format(author.id, len(deleted)))
                    chnl = client.get_channel('465676398036779008')
                    m = "```diff"
                    m += "\n- PURGE -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ In: {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n+ Number: {}".format(number)
                    m += "\n+ Deleted: {}".format(len(deleted))
                    m += "\n```"
                    await client.send_message(chnl, m)
                except:
                    msg.add_field(name=error_img, value="There has been an error while trying to purge messages.")
            except:
                msg.add_field(name=error_img, value="The number has to be a number. Come on, guys, this is simple stuff.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)
    
# ~kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    member = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="No target given.\nExamples:\n`~kick @Tokyo Eating my cookies.`.\n`~kick @Huskie`.")
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles:
                msg.add_field(name=error_img, value="You cannot kick other staff.\nStaff can only be kicked manualy.")
            else:
                chnl = client.get_channel('465676398036779008')
                m = "```diff"
                m += "\n- KICK -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.add_field(name="**User Kicked**", value="<@{}> kicked **{}**!\nNo reason given.".format(author.id, user))
                    await client.kick(user)
                    await client.send_message(chnl, m)
                else:
                    if len(str(args)) > 1000:
                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.add_field(name="**User Kicked**", value="<@{}> kicked **{}**!\nReason:\n{}".format(author.id, user, args))
                        await client.kick(user)
                        await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# ~ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    member = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="No target given.\nExamples:\n`~ban @Huskie Stealing my heart.`.\n`~ban @Tok`.")
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles:
                msg.add_field(name=error_img, value="You cannot ban other staff.\nStaff can only be banned manualy.")
            else:
                chnl = client.get_channel('465676398036779008')
                m = "```diff"
                m += "\n- BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}**!\nNo reason given.".format(author.id, user))
                    await client.ban(user)
                    await client.send_message(chnl, m)
                else:
                    if len(str(args)) > 1000:
                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}**!\nReason:\n{}".format(author.id, user, args))
                        await client.ban(user)
                        await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    author = ctx.message.author
    member = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper = discord.utils.get(ctx.message.server.roles, name='Trial Moderator')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles:
        if userID == None:
            msg.add_field(name=error_img, value="No user ID given.\nExample: `~unban 299761993382887425`.")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            try:
                user = discord.utils.get(banned_users,id=userID)
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="<@{}> unbanned **{}** ( `{}` ).".format(author.id, user, userID))
                m = "```diff"
                m += "\n- UNBAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                chnl = client.get_channel('453219479963303936')
                await client.send_message(chnl, m)
            except:
                msg.add_field(name=error_img, value="There was an error while trying to unban that ID.\nEither the ID you specified doesn't exist or it isn't banned.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# ~hackban <id> <reason>
@client.command(pass_context=True)
async def hackban(ctx, target = None, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x84b5ed, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or manager in author.roles or admin in author.roles:
        if target == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `~idban 299761993382887425 Stealing chocolate.`.")
        else:
            try:
                a = await client.get_user_info(target)
                await client.http.ban(target, server.id, 0)
                msg.add_field(name=":hammer_pick: ", value="<@{}> ID banned **{}**.\nReason:\n{}".format(author.id, a, args))
                m = "```diff"
                m += "\n- ID BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(a, a.id)
                m += "\n+ Reason:"
                m += "\n```"
                m += "\n{}".format(args)
                chnl = client.get_channel('453219479963303936')
                await client.send_message(chnl, m)
            except:
                msg.add_field(name=error_img, value="There was an error while trying to ID ban that user.\nEither the user cannot be banned or the ID you specified doesn't exist.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Admins, Co-Owners and Owners.")
    await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
