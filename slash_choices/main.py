import discord
import asyncio
import config
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('Online.')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
