import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv

tk0='MTQ0ODYxMDUzNz'
tk1='c3MTQ5OTU4M'
tk2='g.GJJQkm.'
tk3='67dKZVO9dPoXjX'
tk4='MTlC8K5CMYGDIePuCuJgSK0E'

load_dotenv()
token = tk0+tk1+tk2+tk3+tk4

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
bot = commands.Bot(command_prefix = '(', intents=intents)

@bot.event
async def on_ready():
    print("logged in")
    
    for fl in os.listdir('./cogs'):
        if fl.endswith('.py'):
            await bot.load_extension(f'cogs.{fl[:-3]}')
    print('cog loaded')



bot.run(token)
