from database.interface import InterfaceStatistic


class Analyser:

    @staticmethod
    def get_data_from_database(event_id: int):

        # Getting raw data
        data = InterfaceStatistic.get_statistic_by_event_id(event_id)
        if len(data) == 0:
            return None

        # Create output format
        output_data = []

        # Create output
        for i in data:
            output_data.append(i.statistic)

        return output_data

    @staticmethod
    def get_data(statistics: list):
        # Create output format
        data = [
            {
                'Паблики': 0,
                'Общее количество': 0,
                'Ответивших': 0,
                'Зарегистрировавшихся': 0
            },
            {
                'Знакомые': 0,
                'Общее количество': 0,
                'Ответивших': 0,
                'Зарегистрировавшихся': 0
            }
        ]
        # Create output
        for statistic in statistics:
            statistic = statistic.split(sep='\n')
            
            for i in range(len(statistic)):
                statistic[i] = statistic[i].split(sep=':')
                statistic[i][1] = int(statistic[i][1])

            for i in range(len(statistic)):
                key, value = statistic[i]
                if i == 0:
                    if value > data[0][key]:
                        data[0].update({key: value})
                elif 1 <= i <= 3:
                    data[0].update({key: data[0][key] + value})
                elif 4 <= i <= 7:
                    data[1].update({key: data[1][key] + value})

        return data

    def get_stats(self, event_id: int):

        data = self.get_data(statistics=self.get_data_from_database(event_id))

        if data is not None:
            output = ""

            for i in range(len(data)):

                for key, value in data[i].items():

                    output += f'{key}: {value}\n'

                if i == 0:

                    output += '\n'

            return output
        else:
            return 'Нет статистики'
