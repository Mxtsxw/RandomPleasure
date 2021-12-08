# bot.py

# Imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Client and Bot setup
client = discord.Client()
bot = commands.Bot(command_prefix=['!', '.', '$'])


@client.event
async def on_ready():
    print(f"RamdomPH Logged as {client.user.name}")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("vaut mieux pas savoir"))


@bot.command(name="greeting")
async def greeting(ctx, member: discord.Member = None):
    print('greeting launch')
    if member:
        await ctx.send(f'Hi {member.name} !')
    else:
        await ctx.send(f'Hi {ctx.author.name} !')


@bot.command(name='video')
async def video(ctx):
    
    print("Command run")
    await ctx.send("A special gift for you")

client.run(TOKEN)

