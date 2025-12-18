import discord
import asyncio
import os
from discord.ext import commands
#放開頭
from flask import Flask
from threading import Thread

tk0='MTQ0ODYxMDUzNz'
tk1='c3MTQ5OTU4M'
tk2='g.GJJQkm.'
tk3='67dKZVO9dPoXjX'
tk4='MTlC8K5CMYGDIePuCuJgSK0E'


token = tk0+tk1+tk2+tk3+tk4

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
bot = commands.Bot(command_prefix = '(', intents=intents)

@bot.event
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
@bot.event
async def on_ready():
    print("logged in")
    
    for fl in os.listdir('./cogs'):
        if fl.endswith('.py'):
            await bot.load_extension(f'cogs.{fl[:-3]}')
    print('cog loaded')


# 放結尾
app = Flask('')

@app.route('/')
def home():
    return "上線了"

def run_flask():
  
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)

async def main():
   
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
 
    async with bot:
        await load_extensions()
        await bot.start(token)

if __name__ == '__main__':
  	asyncio.run(main())
    

