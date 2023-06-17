from structure import Team


class Competition:

    pages_list = ['all', 'particular', 'standings', 'matches', 'teams', 'scorers']
    menu = ('competitions', pages_list)

    def __init__(self, competition: dict, team: Team):

        self.__count = competition['count']

        self.__code_id = competition['competition']['id']
        self.__name = competition['competition']['name']

        self.__info_about = competition['competition']

        self.__season = competition['filters']['season']
        self.__season_details = competition['season']

        self.teams = {i['name']: team(i) for i in competition['teams']}

    def basic_information(self):
        basic_info = dict()

        basic_info['id'] = self.__info_about['id']
        basic_info['sigla'] = self.__info_about['code']
        basic_info['nome'] = self.__info_about['name']
        basic_info['temporada'] = self.__season
        basic_info['total de equipes'] = self.__count
        basic_info['rodada atual'] = self.__season_details['currentMatchday']

        return basic_info

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    def get_acronym(self):
        return self.__info_about['code']
