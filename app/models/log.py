from datetime import datetime
from typing import Union

from discord.abc import Messageable
from PyDrocsid.database import db
from sqlalchemy import Column, Integer, BigInteger, DateTime, String, Enum

from models.channel import ChannelType


class Log(db.Base):
    __tablename__ = "log"

    id: Union[Column, int] = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    timestamp: Union[Column, datetime] = Column(DateTime, default=datetime.utcnow)
    user_id: Union[Column, int] = Column(BigInteger)
    content: Union[Column, str] = Column(String(512))

    channel_id: Union[Column, int] = Column(BigInteger, nullable=True)
    channel_type: Union[Column, ChannelType] = Column('channel_type', Enum(ChannelType))

    @staticmethod
    def create(user_id: int, content: str, channel: Messageable) -> "Log":
        row = Log(
            user_id=user_id,
            content=content,
            channel_id=channel.id,
            channel_type=ChannelType.get_type(channel)
        )
        db.add(row)
        return row
