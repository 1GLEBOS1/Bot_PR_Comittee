from peewee import DoesNotExist
from aiogram.dispatcher.filters.filters import BoundFilter
from aiogram import types
from database.interface import InterfacePRCommitteeMember


class IsOwnerFilter(BoundFilter):
    """
    Custom filter 'is_owner'
    """

    key = 'is_owner'

    def __init__(self, is_owner):
        self.is_owner = is_owner

    async def check(self, message: types.Message):
        try:
            InterfacePRCommitteeMember.get_owner_id()
            return message.from_user.id == InterfacePRCommitteeMember.get_owner_id()
        except DoesNotExist:
            return False


class IsChairmanFilter(BoundFilter):
    """
    Custom filter 'is_chairman'
    """

    key = 'is_chairman'

    def __init__(self, is_chairman):
        self.is_chairman = is_chairman

    async def check(self, message: types.Message):
        try:
            InterfacePRCommitteeMember.get_chairman_id()
            return message.from_user.id == InterfacePRCommitteeMember.get_chairman_id()
        except DoesNotExist:
            return False


class IsPRComitteeMemberFilter(BoundFilter):
    """
    Custom filter 'is_pr_comittee_member'
    """

    key = 'is_pr_comittee_member'

    def __init__(self, is_pr_comittee_member):
        self.is_pr_comittee_member = is_pr_comittee_member

    async def check(self, message: types.Message):
        return message.from_user.id in InterfacePRCommitteeMember.get_pr_mambers_id()
