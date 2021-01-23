from enum import Enum

from discord import TextChannel, DMChannel, GroupChannel, VoiceChannel
from discord.abc import Messageable


class ChannelType(Enum):
    TEXT, DM, GROUP, VOICE = range(4)

    @staticmethod
    def get_type(channel: Messageable) -> "ChannelType":
        return {
            TextChannel: ChannelType.TEXT,
            DMChannel: ChannelType.DM,
            GroupChannel: ChannelType.GROUP,
            VoiceChannel: ChannelType.VOICE,
        }[type(channel)]
