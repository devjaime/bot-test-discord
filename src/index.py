import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

from twitter_scraper import get_trends, get_tweets

#libreria verifica dispositivo wifi
import sys
import subprocess
import os 
from decouple import config

#librerias selenium
from urllib.request import Request, urlopen
import json
from selenium import webdriver #pip install selenium for this package to work
import time

bot = commands.Bot(command_prefix='? ', description="this is helper bot")

@bot.command()
async def Salir(ctx):

    GOOGLEMAPSEMERGENCY=config('GOOGLEMAPSEMERGENCY')
    driver = webdriver.Firefox()
    driver.get(GOOGLEMAPSEMERGENCY)

    #await ctx.send('Se a abierto en el navegador el ultimo video dispnible')
    subprocess.Popen(["say", "ok google, turn of room"])
    await ctx.send(GOOGLEMAPSEMERGENCY)
    await ctx.send('Tuve que salir rapido!!, por unos momento, vuelvo en cuanto pueda. En el pc deje la dirección donde estoy y como llegar')
    
    
    IP_NETWORK = config('IP_CONFIG')
    IP_DEVICE = config('IP_DEVICE') + ":"

    proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
    while True:
    
        line = proc.stdout.readline()
        if not line:
            break
        #the real code does filtering here
        connected_ip = line.decode('utf-8').split()[3]
        if connected_ip != IP_DEVICE:
            print("El invitado no a llegado - " + IP_NETWORK +  " -  " + IP_DEVICE)
        if connected_ip == IP_DEVICE:
            print("El invitado acaba de llegar")
            subprocess.Popen(["say", "ok google, turn on lights"])
            time.sleep(15)
            subprocess.Popen(["say", "ok google, play yoga music on spotify"])
            print("Musica relajante")
            time.sleep(15)
            subprocess.Popen(["say", "ok google, script"])
            print("Saludar al invitado")
            time.sleep(15)
            await ctx.send('Activando rutina vuelta a casa')

            API_KEYVIDEO=config('API_KEYVIDEO')
            CHANNEL_ID=config('CHANNEL_ID')
            BASE_SEARCH_URL=config('BASE_SEARCH_URL')

            api_keyvideo = API_KEYVIDEO
            channel_id =CHANNEL_ID
            base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
            
            url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_keyvideo, channel_id)

            headers = {"User-Agent": "XYZ/3.0"}
            reqinp = Request(url, headers = headers)
            webpage = urlopen(reqinp).read()

            data = webpage

            resp = json.loads(data)
            
            vidID = resp['items'][0]['id']['videoId']
            base_video_url='https://www.youtube.com/watch?v='
            await ctx.send(base_video_url + vidID)
            TAREASDIARIAS=config('TAREASDIARIAS')
            driver = webdriver.Firefox()
            driver.get(TAREASDIARIAS)
            break

@bot.command()
async def Invitado(ctx):
    IP_NETWORK = config('IP_CONFIG')
    IP_DEVICE = config('IP_DEVICE') + ":"

    proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
    while True:
    
        line = proc.stdout.readline()
        if not line:
            break
        #the real code does filtering here
        connected_ip = line.decode('utf-8').split()[3]
        if connected_ip != IP_DEVICE:
            print("El invitado no a llegado - " + IP_NETWORK +  " -  " + IP_DEVICE)
        if connected_ip == IP_DEVICE:
            print("El invitado acaba de llegar")
            subprocess.Popen(["say", "Hello!"])
            print("Encender Luces")
            print("Enceder aire acondicionado")
            print("Abrir cortinas")
            print("Encender la televisión")
            print("Correr rutina de google home")
            print("Automatizar procesos de resguardo de archivos en pc personal")
            print("Notificarme por correo que la persona esta en casa")
            

            await ctx.send('El invitado a llegado!!, se activara el protocolo de visita')
            break

@bot.command()
async def ping(ctx):
    await ctx.send('el servicio esta ejecutandose')


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
# mercado libre


@bot.command()
async def mercado(ctx, *, search):
    query_string = parse.urlencode({'/': search})
    html_content = request.urlopen(
        'https://listado.mercadolibre.cl' + query_string)
    await ctx.send(html_content)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Información bot",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)


@bot.command()
async def twit(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Información twit",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="Twit relevantes", value=f"{get_trends()}")
    for tweet in get_tweets('#python', pages=1):
        embed.add_field(name="Twit de mi cuenta", value=f"{tweet['text']}")

    await ctx.send(embed=embed)


@bot.command()
async def codigo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Quincy Larson",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    for tweet in get_tweets('#freecodecamp', pages=1):
        embed.add_field(name="Twit", value=f"{tweet['text']}")

    await ctx.send(embed=embed)


@bot.command()
async def covid(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Covid19",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    for tweet in get_tweets('#covid19 chile', pages=1):
        embed.add_field(name="Twit", value=f"{tweet['text']}")

    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(
        r"watch\?v=(\S{11})", html_content.read().decode())
    # print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
# Events


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print('Bot activo en este momento')
    subprocess.Popen(["say", "bot activate"])
API_KEYDISCORD = config('API_KEYDISCORD')
bot.run(API_KEYDISCORD)
