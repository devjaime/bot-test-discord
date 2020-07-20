import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

from twitter_scraper import get_trends, get_tweets

bot = commands.Bot(command_prefix='?', description="this is helper bot")


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
    for tweet in get_tweets('HsJhernandez', pages=1):
        embed.add_field(name="Twit de mi cuenta", value=f"{tweet['text']}")

    await ctx.send(embed=embed)


@bot.command()
async def codigo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Quincy Larson",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    for tweet in get_tweets('ossia', pages=1):
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
bot.run('debesponertutokenaqui')
