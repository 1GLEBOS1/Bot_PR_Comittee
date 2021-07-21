from aiogram.dispatcher.filters.filters import BoundFilter
from aiogram import types


class IsOwnerFilter(BoundFilter):
    """
    Custom filter 'is_owner'
    """

    key = 'is_owner'

    def __init__(self, is_owner):
        self.is_owner = is_owner

    async def check(self, message: types.Message):
        return message.from_user.id == 870069981


class IsChairmanFilter(BoundFilter):
    """
    Custom filter 'is_chairman'
    """

    key = 'is_chairman'

    def __init__(self, is_chairman):
        self.is_chairman = is_chairman

    async def check(self, message: types.Message):
        return False


class IsPRComitteeMemberFilter(BoundFilter):
    """
    Custom filter 'is_pr_comittee_member'
    """

    key = 'is_pr_comittee_member'

    def __init__(self, is_pr_comittee_member):
        self.is_pr_comittee_member = is_pr_comittee_member

    async def check(self, message: types.Message):
        pass
