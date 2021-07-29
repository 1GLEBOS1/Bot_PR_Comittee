from .database_connection import PRCommitteeMember as PR, Statistic


class InterfacePRCommitteeMember:
    """
    This class is interface of table PRCommitteMember
    """
    @staticmethod
    def get_owner_id():
        """
        This function returns telegram id of owner from database
        """
        owner = PR.get(PR.access_level == 5)
        return owner.telegram_id

    @staticmethod
    def get_chairman_id():
        """
        This function returns telegram id of chairman from database
        """
        chairman = PR.get(PR.access_level == 4)
        return chairman.telegram_id

    @staticmethod
    def get_pr_mambers_id():
        """
        This function returns list of telegram id pr men from database
        """
        pr_mans = PR.select().where(PR.access_level == 3)
        telegram_ids = [person.telegram_id for person in pr_mans]
        return telegram_ids

    @staticmethod
    def add_member(telegram_id: int, name: str, access_level: int, position):
        """
        This function adds statistic to database
        """
        PR.create(telegram_id=telegram_id, access_level=access_level, name=name, position=position)

    @staticmethod
    def create_db():
        PR.create_table()

    @staticmethod
    def get_members():
        members = PR.select().where(PR.id != 0)
        output = ""
        for member in members:
            output += f"id: {member.id}, tg id: {member.telegram_id}, name: {member.name} " \
                      f"access level: {member.access_level}, position: {member.position}\n"
        return output

    @staticmethod
    def delete_member(telegram_id: int):
        member = PR.delete().where(PR.telegram_id == telegram_id)
        member.execute()


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

    def get_statistic_(self, event_id: int):
        data = self.get_statistic(event_id)
        output = ""
        for i in data:
            output += f"id: {i.id}, event id: {i.event_id}, author id: {i.author_id} " \
                      f"stats: {i.statistic}\n"
        return output
