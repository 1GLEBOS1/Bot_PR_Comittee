from .database_connection import PRCommitteeMember, Statistic


class InterfacePRCommitteeMember:
    """
    This class is interface of table PRCommitteMember
    """
    @staticmethod
    def get_owner_id():
        """
        This function returns telegram id of owner from database
        """
        owner = PRCommitteeMember.get(PRCommitteeMember.access_level == 5)
        return owner.telegram_id

    @staticmethod
    def get_chairman_id():
        """
        This function returns telegram id of chairman from database
        """
        chairman = PRCommitteeMember.get(PRCommitteeMember.access_level == 4)
        return chairman.telegram_id

    @staticmethod
    def get_pr_mambers_id():
        """
        This function returns list of telegram id pr men from database
        """
        pr_mans = PRCommitteeMember.select().where(PRCommitteeMember.access_level == 3)
        telegram_ids = [person.telegram_id for person in pr_mans]
        return telegram_ids

    @staticmethod
    def add_member(telegram_id: int, name: str, access_level: int, position):
        """
        This function adds statistic to database
        """
        PRCommitteeMember.create(telegram_id=telegram_id, access_level=access_level, name=name, position=position)

    @staticmethod
    def create_db():
        PRCommitteeMember.create_table()


class InterfaceStatistic:
    """
    This class is interface of table Statistic
    """

    @staticmethod
    def add_statistic(statistic: str, author_id: int, event_id: int):
        """
        This function adds statistic to database
        """
        Statistic.create(author_id=author_id, event_id=event_id, statistic=statistic)

    @staticmethod
    def get_statistic(event_id: int):
        """
        This function returns full statistic of event
        """
        raw_data = Statistic.select().where(Statistic.event_id == event_id)
        output_data = [data for data in raw_data]
        return output_data

    @staticmethod
    def create_db():
        Statistic.create_table()
