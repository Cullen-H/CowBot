import discord
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['Clear'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)

    

def setup(client):
    client.add_cog(Clear(client))
