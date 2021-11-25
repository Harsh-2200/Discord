import discord
from discord.ext import commands
from discord.flags import Intents
import music

cogs = [music]

client = commands.Bot(command_prefix="!" , Intents = discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("OTExODQ5MDA0NTU4NjEwNDcy.YZnXkA.suhyBKHFJICk_nMS1MgZT0uKLgM")

 