import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self , client ):
        self.client = client

    @commands.command()
    async def join(self , ctx):
        if ctx.author.voice is None:
            await ctx.send("bsdk voice channel tho join kr lo ")
        voice_channel = ctx.auth.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self , ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self , ctx , url ):
        if ctx.voice_client.stop():
            FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_deelay' }




def setup(client):
    client.add_cog(music(client))



