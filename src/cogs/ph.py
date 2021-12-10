import discord
from discord.ext import commands
from pornhub_api import PornhubApi
import random


api = PornhubApi()


class Ph(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('PH Video loaded successfully')

    @commands.command()
    async def video(self, ctx):
        tags = random.sample(api.video.tags("f").tags, 5)
        category = random.choice(api.video.categories().categories)
        result = api.search.search(ordering="mostviewed", tags=tags, category=category)

        videos = []
        for vid in result.videos:
            videos.append(vid)
        
        video = random.choice(videos)
        await ctx.author.send(video.url)


def setup(client):
    client.add_cog(Ph(client))
