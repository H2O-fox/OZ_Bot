import discord
from discord.ext import commands
from OZ_Bot.core.classes import Cog_Extension
import json
from discord import member

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
       channel=self.bot.get_channel(int(jdata['Welcome_channel']))
       await channel.send(f'{member} join!')
       print(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
       channel=self.bot.get_channel(int(jdata['Leave_channel']))
       await channel.send(f'{member} leave!')
       print(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('hi')
        

def setup(bot):
    bot.add_cog(Event(bot))