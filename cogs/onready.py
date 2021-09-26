import discord
from discord.ext import commands

class OnReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('No mooooo'))
        print('Bot is online.')

def setup(client):
    client.add_cog(OnReady(client))


