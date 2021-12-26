import discord
from discord.ext import commands
import random

from discord.ext.commands.errors import PrivateMessageOnly


class Roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('PH Video loaded successfully')

    @commands.command()
    async def roll(self, ctx):
        if random.randint(1, 3) == 3:
            print(f"{ctx.author} has been Rickrolled")
            await ctx.author.send("https://youtu.be/dQw4w9WgXcQ")
        else:
            await ctx.message.add_reaction("💥")


def setup(client):
    client.add_cog(Roll(client))
