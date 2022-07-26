import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['kun', 'Kun', '張彥坤', '彥坤', '坤']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('好帥')
        elif msg.content.endswith('林亮儀') and msg.author != self.bot.user:
            await msg.channel.send('超笨')

def setup(bot):
    bot.add_cog(Event(bot))