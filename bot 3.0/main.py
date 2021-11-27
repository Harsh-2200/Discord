from discord.ext import commands
from chatbot import chat
bot = commands.Bot(command_prefix="!")


bot.lava_nodes = [
    {
        'host' : 'lava.link',
        'port' : 80,
        'rest_uri' : f'http://lava.link:80',
        'identifier' : 'MAIN' ,
        'password' : 'anything', 
        'region' : 'india'
    }
]

@bot.event
async def on_ready():
    print("Bot is ready to play music")
    bot.load_extension('dismusic')



@bot.command()
async def bi(ctx):
    await ctx.send(chat())

@bot.command()
async def hi(ctx):
    await ctx.send("Hello")
   


bot.run('')



