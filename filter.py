from aiogram.dispatcher.filters.filters import BoundFilter
from aiogram import types


class IsOwnerFilter(BoundFilter):
    """
    Custom filter 'is_owner'
    """

    key = 'is_owner'

    def __init__(self, is_owner):
        self.is_owner = is_owner

    def check(self, message=types.Message):
        pass


class IsChairmanFilter(BoundFilter):
    """
    Custom filter 'is_chairman'
    """

    key = 'is_chairman'

    def __init__(self, is_chairman):
        self.is_chairman = is_chairman

    def check(self, message=types.Message):
        pass


class IsPRComitteeMemberFilter(BoundFilter):
    """
    Custom filter 'is_pr_comittee_member'
    """

    key = 'is_pr_comittee_member'

    def __init__(self, is_pr_comittee_member):
        self.is_pr_comittee_member = is_pr_comittee_member

    def check(self, message=types.Message):
        pass


class IsOwnerOrChairmanFilter(BoundFilter):

    key = 'is_owner_or_chairman'

    def __init__(self, is_owner_or_chairman):
        self.is_owner_or_chairman = is_owner_or_chairman

    def check(self):
        pass
