import discord
from discord.ext import commands
from discord_bot.core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):  #打[ping來查看當前延遲
        await ctx.send(F'{round(self.bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(Main(bot))