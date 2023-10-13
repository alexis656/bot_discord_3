import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

# Lista de nombres de archivos de memes (sin extensiones)
meme_list = ["meme1", "meme2"]

@bot.command()
async def meme(ctx):
    img_name = random.choice(meme_list)  # Elige un nombre de archivo al azar
    with open(f'imagen/{img_name}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
meme_futbol = ["meme3", "meme4","meme5"]

@bot.command()
async def memefut(ctx):
    img_name2 = random.choice(meme_futbol)  # Elige un nombre de archivo al azar
    with open(f'imagen/{img_name2}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("MTE1NTIwMTc5ODI0MDQ4NTUyNg.GpiaTA.7PPFc5AHVTzbglUcye2aGgv1Oal9JOoKwiGmQA")
