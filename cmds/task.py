import discord
from discord.ext import commands, tasks
from discord_bot.core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(993905087502090300)
            while not self.bot.is_closed():
                await self.channel.send("Hi there!")
                await asyncio.sleep(5) #單位:秒
        self.bg_task = self.bot.loop.create_task(interval())

def setup(bot):
    bot.add_cog(Task(bot))