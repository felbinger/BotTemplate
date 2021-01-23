from enum import auto
from typing import Union

from PyDrocsid.permission import BasePermission, BasePermissionLevel
from PyDrocsid.settings import Settings
from discord import Member, User


class Permission(BasePermission):
    change_prefix = auto()
    admininfo = auto()
    view_own_permissions = auto()
    view_all_permissions = auto()

    @property
    def default_permission_level(self) -> "BasePermissionLevel":
        return PermissionLevel.ADMINISTRATOR


class PermissionLevel(BasePermissionLevel):
    PUBLIC, SUPPORTER, MODERATOR, ADMINISTRATOR, OWNER = range(5)

    @classmethod
    async def get_permission_level(cls, member: Union[Member, User]) -> "PermissionLevel":
        if member.id == 251344185783746560:
            return PermissionLevel.OWNER

        if not isinstance(member, Member):
            return PermissionLevel.PUBLIC

        roles = {role.id for role in member.roles}

        async def has_role(role_name):
            return await Settings.get(int, role_name + "_role") in roles

        if member.guild_permissions.administrator or await has_role("admin"):
            return PermissionLevel.ADMINISTRATOR
        if await has_role("mod"):
            return PermissionLevel.MODERATOR
        if await has_role("supp"):
            return PermissionLevel.SUPPORTER

        return PermissionLevel.PUBLIC
