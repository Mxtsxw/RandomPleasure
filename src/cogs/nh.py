import discord
from discord.ext import commands
import random
# from NHentai import NHentai

# nhentai = NHentai()

# -- Nhentai API Unavailabe in France


class Nh(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('NH Video loaded successfully')


    # Unavailabe in France
    # @commands.command()
    # async def pleasure(self, ctx):

    #     random = nhentai.get_random()
    #     await ctx.author.send(random.url)

def setup(client):
    client.add_cog(Nh(client))
