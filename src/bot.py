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
client = commands.Bot(command_prefix=['!', '.', '$'])



@client.event
async def on_ready():
    print(f"RamdomPH Logged as {client.user.name}")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("vaut mieux pas savoir"))


@client.command(name="greeting")
async def greeting(ctx, member: discord.Member = None):
    print('greeting launch')
    if member:
        await ctx.send(f'Hi {member.name} !')
    else:
        await ctx.send(f'Hi {ctx.author.name} !')



# Managing Cogs

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


if __name__ == '__main__':
    for filenames in os.listdir('./cogs'):
        if filenames.endswith('.py'):
            client.load_extension(f'cogs.{filenames[:-3]}')
        

    

client.run(TOKEN)

