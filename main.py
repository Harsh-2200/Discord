import discord
from discord.ext import commands
from discord.flags import Intents
import music

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup()

client = commands.Bot(command_prefix="?" , Intents = discord.Intents.all())

client.run("f51229202fddeda2f450e63f613f73a065245f35c455ff91554fd7ba07b20b90")

 