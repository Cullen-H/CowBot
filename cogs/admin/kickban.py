import discord
from discord.ext import commands

class KickBan(commands.Cog):
    
    def __init__(self, client):                
        self.client = client
    
    @commands.command(aliases=['Kick'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=1)

    @commands.command(aliases=['Ban'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, * , reason=None):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)

    @commands.command(aliases=['Unban'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        await ctx.channel.purge(limit=1)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return

def setup(client):
    client.add_cog(KickBan(client))
