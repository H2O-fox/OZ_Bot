import discord
from discord.ext import commands
from OZ_Bot.core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
  
    @commands.command()
    async def ping(self, ctx):
       await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('123')

    @commands.command()
    async def em(self, ctx):
       embed=discord.Embed(title="About", url="https://www.youtube.com", description="About a bot", color=0xd00b0b, timestamp=datetime.datetime.now())
       embed.set_author(name="H2Ofox", url="https://twitter.com/home", icon_url="https://cdn3.iconfinder.com/data/icons/capsocial-round/500/youtube-512.png")
       embed.set_thumbnail(url="https://cdn3.iconfinder.com/data/icons/capsocial-round/500/youtube-512.png")
       embed.add_field(name="1", value="11", inline=False)
       embed.add_field(name="2", value="22", inline=True)
       embed.add_field(name="3", value="33", inline=True)
       embed.add_field(name="4", value="44", inline=True)
       embed.set_footer(text="123456")
       await ctx.send(embed=embed)
      
    @commands.command()
    async def sayd(self, ctx, msg):
        await ctx.message.delete()
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Main(bot))