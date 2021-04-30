import re
import os
import time
import discord
from youtube_dl import YoutubeDL
from discord.ext import commands
from urllib.parse import urlencode
from urllib.request import urlopen

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Ready and listening as {0.user}".format(client))

@client.command()
async def join(ctx):
    await ctx.message.author.voice.channel.connect()

@client.command()
async def play(ctx, uri:str):
    if ctx.author.voice:
        await ctx.message.author.voice.channel.connect()

        ydl_opts = {'format': 'bestaudio'}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(uri, download = False)
            url = info['formats'][0]['url']

        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        voice.play(discord.FFmpegPCMAudio(url))

    else:
        await ctx.send("{0}, you must be connected to a voice channel!".format(ctx.message.author.name))

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Music is paused or either not playing!")

@client.resume()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Music is already playing!")

@client.command()
async def stop(ctx):
    discord.utils.get(client.voice_clients, guild = ctx.guild).stop()

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    if voice:
        await voice.disconnect()
    else:
        await ctx.send("I'm not connected to any voice channel")

@client.command()
async def yt(ctx, *, search_string):
    query_string = urlencode({'search_query': search_string})
    search_results = urlopen('http://www.youtube.com/results?' + query_string)

    result_links = re.findall(r'/watch\?v=(.{11})', search_results.read().decode())

    await ctx.send('http://www.youtube.com/watch?v=' + result_links[0])

@client.command()
async def extract(ctx, url:str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '<your_destination_path>/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    name = ""
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        name = str(ydl.extract_info(url, download=False)['title'])

client.run('<your_bot_token>')
