# Bot de discord python

Cuenta de Discord
Antes de empezar necesitas ser propietario de un servidor o tener permisos para poder ejecutar tu bot en uno.

Agregando tu Bot a tu Server
Antes de programar un bot, lo primero que necesitamos, es agregarlo al servidor al que queremos que nos ayude a administrar.

Visita el sitio web de Discord para desarrolladores. Crea un aplicación y colocale un nombre, en mi caso lo voy a llamar Test App, en su pestaña Bot, crea un nuevo bot, colocale un nombre, en mi caso lo voy a llamar pythonbot, luego ve a la pestaña OAuth, en permisos selecciona bot. esto te dara una dirección que deberias usar para autorizar tu bot, seleccióna tu servidor, y listo, tu bot ahora ya esta adentro de tu server.

Adicionalmente, ya que hemos creado nuestro bot, ahora tendremos acceso a un TOKEN, que es como tener una contraseña para nuestra aplicación.

### Programando el Bot con Python
Para poder programar nuestro bot con python, haremos uso de una biblioteca de python llamada python.py, para poder instalarla puedes ejecutar el siguiente comando.
```python
pip install discord.py
```

Cabe resaltar, que una version de Python3.5 o versiones más nuevas, es necesario.

* Creemos nuestro primer bot. La tarea es simple, cada vez que tipeemos el comando ">ping", queremos recibir el mensaje "pong".
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')
```

* Ejecuta este script, y pruebalo tipeando en tu servidor de Discord el comando >ping.

* Para aceptar parametros de los comandos, puedes simplemente agregar más parametros a la funcion. El siguiente comando, permite sumar dos numeros.

```python
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
```

Para probarlo tipea en tu servidor

>sum 12 20

* El bot como respuesta te debería mostrar la suma 32. Ahora, intenta crear las otras operaciones matematicas para tu bot.

* Eventos
```python
@bot.event
async def on_ready():
    game = discord.Game('Developing the API')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('My Ready is Body')
```

* Y en cuanto al evento de Streamming, podemos hacerlo así.
```python
await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/faztgame"))
````

* Cabe resaltar que la URL, tiene que ser una de Twitch.

Mensajes
* en cuanto a los mensajes, podemos procesarlos con otro evento llamado on_message. agrega este otro evento adicionalmente al que ya tenemos escrito.

```python
@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)
```
Embed Messages
* en cuanto a los mensajes enriquecidos, puedes hacerlo usando el metodo embed.
```python
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)
```
* Usando los comandos puedes hacer practicamente cualquier cosa. Lo más tipico es integrarlo a otros servicios de la Web, como Youtube, Spotify y así. A continuación te muestro un comando que te permite hacer busquedas en youtube.
```python
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(
        r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
```

* Puede traer información de un hash o una cuenta asociada para twitter y conocer la información paginada

```python
@bot.command()
async def twit(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Información twit",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="Twit relevantes", value=f"{get_trends()}")
    for tweet in get_tweets('HsJhernandez', pages=1):
        embed.add_field(name="Twit de mi cuenta", value=f"{tweet['text']}")

    await ctx.send(embed=embed)
```

* Finalmente te recomiendo visitar estos enlaces, para conocer más:
https://discordpy.readthedocs.io/en/latest/index.html
api scrapping de twitter
* https://pypi.org/project/twitter-scraper/ 