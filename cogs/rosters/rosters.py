import discord
from discord.ext import commands
import models.models as models

class Rosters(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def SetRosterChannel(self, ctx):
    """Set template directory"""
    for channel in ctx.guild.channels:
      if channel.name == channelName
        channel_id = channel.id
        db.SetRosterChannel(channel_id, ctx.guild.id)

  async def GetRoster(self, ctx, roster_name)
  """Get template from roster"""
    channel = client.get_channel(db.getRosterId(ctx.guild.id))
    messages = await ctx.channel.history(limit=200).flatten()

    for msg in messages:
      if msg[:len(roster_name)-1] == roster_name:
        dm = await message.author.create_dm()
        await dm.send(msg(len(roster_name-1:])
        return

  def setup(client):
    client.add_cog(Rosters(client))
