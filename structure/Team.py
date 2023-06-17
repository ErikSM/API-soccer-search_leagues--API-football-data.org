

class Team:

    pages_list = ['all', 'particular', 'matches']
    menu = ('teams', pages_list)

    def __init__(self, team: dict):

        self.__area = team['area']

        self.__code_id = team['id']
        self.__name = team['name']

        self.details = {
            "nome popular": team['shortName'],
            "sigla": team['tla'],
            "escudo": team['crest'],
            "endereco": team['address'],
            "website": team['website'],
            "fundacao": team['founded'],
            "cores do clube": team['clubColors'],
            "estadio": team['venue'],
            "ultima atualizacao": team['lastUpdated']
        }

        self.advanced_info = {
            'tecnico': team['coach'],
            'jogadores': team['squad'],
            'outros membros': team['staff'],
            'competicoes': {i['name']: i
                            for i in team['runningCompetitions']}
        }

    def basic_information(self):
        basic_info = dict()

        basic_info['nome'] = self.__name
        basic_info['estadio'] = self.details['estadio']
        basic_info['total de competicoes disputadas'] = len(self.advanced_info['competicoes'])
        basic_info['ultima atualizacao'] = self.details['ultima atualizacao']

        return basic_info

    def main_data(self):
        other_info = self.advanced_info.copy()
        other_info['detalhes'] = self.details.copy()

        return other_info

    @property
    def area(self):
        return self.__area

    @property
    def code_id(self):
        return self.__code_id

    @property
    def name(self):
        return self.__name

    def get_acronym(self):
        return self.details['sigla']
