import re
import os
import time
import discord
import youtube_dl
from discord.ext import commands
from urllib.parse import urlencode
from urllib.request import urlopen

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Ready and listening as {0.user}".format(client))

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
