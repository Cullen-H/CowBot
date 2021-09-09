import discord
from discord.ext import commands
from models.roster import RosterChannel

class Rosters(commands.Cog):
    """Handles roster templates"""

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['SetRosterChannel'])
    @commands.has_permissions(administrator=True)
    async def set_roster_channel(self, ctx):
        """Set template directory"""
        
        channel_id = ctx.message.channel.id
        try:
            RosterChannel.set(ctx.guild.id, channel_id)
            await ctx.send(f'Channel Set to id {channel_id}')
        except Exception as e:
            print('Error: ', e)
    
    @commands.command(aliases=['Roster', 'roster'])
    async def get_roster(self, ctx, roster_name):
        """Get template from roster"""

        channel = self.client.get_channel(RosterChannel.get(ctx.guild.id))
        messages = await channel.history(limit=200).flatten()

        for msg in messages:
            if msg.content[:len(roster_name)] == roster_name:
                dm = await msg.author.create_dm()
                await dm.send(msg.content)
                return

def setup(client):
    client.add_cog(Rosters(client))
