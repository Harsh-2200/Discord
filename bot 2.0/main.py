from discord.ext import commands

bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    print("Bot is ready to play music")


bot.run(' ')



