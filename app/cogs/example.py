from typing import Optional

from PyDrocsid.database import db_thread
from discord import Guild, Message
from discord.ext.commands import Cog, Bot

from models.log import Log
from util import get_prefix


class Example(Cog, name="Example"):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.guild: Optional[Guild] = None

    async def on_ready(self):
        self.guild: Optional[Guild] = self.bot.guilds[0]

    async def on_message(self, message: Message):
        if message.content.startswith(await get_prefix()):
            return
        if message.author.bot:
            return
        await db_thread(Log.create, message.author.id, message.content, message.channel)
