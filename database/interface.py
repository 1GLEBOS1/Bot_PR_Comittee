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

    @staticmethod
    def get_members():
        members = PRCommitteeMember.select().where(PRCommitteeMember.id != 0)
        output = ""
        for member in members:
            output += f"id: {member.id}, tg id: {member.telegram_id}, name: {member.name} " \
                      f"access level: {member.access_level}, position: {member.position}\n"
        return output

    @staticmethod
    def delete_member(telegram_id: int):
        member = PRCommitteeMember.delete().where(PRCommitteeMember.telegram_id == telegram_id)
        member.execute()

    @staticmethod
    def get_telegram_id(id_: int):
        user = PRCommitteeMember.get(PRCommitteeMember.id == id_)
        return user.telegram_id

    @staticmethod
    def get_id_by_telegram_id(telegram_id: int):
        user = PRCommitteeMember.get(PRCommitteeMember.telegram_id == telegram_id)
        return user.id


class InterfaceStatistic:
    """
    This class is interface of table Statistic
    """

    @staticmethod
    def create_db():
        Statistic.create_table()

    @staticmethod
    def add_statistic(statistic_: str, author_id_: int, event_id_: int):
        """
        This function adds statistic to database
        """
        Statistic.create(author_id=author_id_, event_id=event_id_, statistic=statistic_)

    @staticmethod
    def get_statistic_by_event_id(event_id: int):
        """
        This function returns full statistic of event
        """
        query = Statistic.select().where(Statistic.event_id == event_id)
        output_data = [data for data in query]
        return output_data

    @staticmethod
    def get_statistic_by_id(id_: int):
        """
        This function returns full statistic of event
        """
        record = Statistic.get(Statistic.id == id_)
        return record

    @staticmethod
    def get_statistic_by_author_id(author_id: int):
        query = Statistic.select().where(Statistic.author_id == author_id)
        output_data = [data for data in query]
        return output_data

    def get_statistic(self, type_of_data: str, needed_id: int):

        if type_of_data == "author":
            data = self.get_statistic_by_author_id(needed_id)
        elif type_of_data == "event":
            data = self.get_statistic_by_event_id(needed_id)
        else:
            raise TypeError("Unknown type of sorting")

        output = ""
        for i in data:
            output += f"id: {i.id}, event id: {i.event_id}, " \
                      f"author id: {InterfacePRCommitteeMember.get_telegram_id(i.author_id)}, stats: {i.statistic}\n"

        return output

    @staticmethod
    def change_author_id(id_: int, new_author_id: int):
        record = InterfaceStatistic.get_statistic_by_id(id_)
        record.author_id = InterfacePRCommitteeMember.get_telegram_id(
            InterfacePRCommitteeMember.get_id_by_telegram_id(new_author_id)
        )
        record.save()

    @staticmethod
    def delete_statistic(id_: int):
        stats = Statistic.get(Statistic.id == id_)
        stats.delete_instance()
