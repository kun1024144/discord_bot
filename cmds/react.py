import discord
from discord.ext import commands
from discord_bot.core.classes import Cog_Extension
import random
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def picture(self, ctx): #打[picture產生隨機以存取的圖片
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def web(self, ctx):  #打[web產生隨機以存取的圖片
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))