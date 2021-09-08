import discord
from discord.ext import commands
from pathlib import Path
import logging
from disctoken import TOKEN

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = '.')

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    await ctx.send('loaded')
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    await ctx.send('unloaded')
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

paths = Path('./cogs').glob('**/*.py')
for path in paths:
    cog_name = str(path).replace('/', '.')[:-3]
    client.load_extension(cog_name)

client.run(TOKEN) # unique discord bot id
