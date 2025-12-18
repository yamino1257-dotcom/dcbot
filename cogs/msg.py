import discord
from discord.ext import commands
from discord import app_commands
import asyncio as asy

class Msg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name=':')
    async def on_msg(self, ctx, cmd='m', msg='fla fikorod yaminovt', *kw):
        prm=ctx.author.id in [1423889759847059547, ]
        if cmd=='m' and prm:
            await ctx.send(f'{msg}')
        if cmd=='mul' and prm:
            await ctx.send('\n'.join(msg for _ in range(int(kw[0]) if kw else 10)))
        if cmd=='showid':
            await ctx.send(f'{ctx.author.id}')

async def setup(bot):
    await bot.add_cog(Msg(bot))
