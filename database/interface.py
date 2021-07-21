from database_connection import PRCommitteeMember, Statistic


class InterfacePRCommitteeMember:
    """
    This class is interface of table PRCommitteMember
    """
    @staticmethod
    def get_owner_id():
        """
        This function returns telegram id of owner from database
        """
        return PRCommitteeMember.get(PRCommitteeMember.access_level == 1).telegram_id

    @staticmethod
    def get_chairman_id():
        """
        This function returns telegram id of chairman from database
        """
        return PRCommitteeMember.get(PRCommitteeMember.access_level == 2).telegram_id

    @staticmethod
    def get_pr_mamber_ids():
        """
        This function returns list of telegram id pr men from database
        """
        pr_mans = PRCommitteeMember.select().where(PRCommitteeMember.access_level == 3).get()
        for i in range(len(pr_mans)):
            pr_mans[i] = pr_mans[i].telegram_id
        return pr_mans

    @staticmethod
    def add_member(telegram_id: int, name: str, access_level: int, position):
        """
        This function adds statistic to database
        """
        PRCommitteeMember.create(telegram_id=telegram_id, access_level=access_level, name=name, position=position)
