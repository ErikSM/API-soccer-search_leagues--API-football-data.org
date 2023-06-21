from access.ApiAccess import ApiAccess


def access_team_dict(team_code):
    access = ApiAccess(Team.options, 'particular', team_code)
    team_dict = access.open_required_dict()

    return team_dict


class Team:
    pages_list = ['all', 'particular', 'matches']
    options = ('teams', pages_list)

    all_teams = ApiAccess(options)

    def __init__(self, data_dict_or_data_code, data_is_dict=True):

        if data_is_dict:
            team = data_dict_or_data_code
        else:
            team = access_team_dict(data_dict_or_data_code)

        self.__code_id = team['id']
        self.__name = team['name']
        self.__area = team['area']

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

        self.coach = team['coach'],
        self.squad = team['squad'],
        self.staff = team['staff'],

        self.running_competiitions = {i['name']: i
                                      for i in team['runningCompetitions']}

        self.matches = None

    def basic_information(self):
        basic_info = dict()

        basic_info['nome'] = self.__name
        basic_info['estadio'] = self.details['estadio']
        basic_info['total de competicoes disputadas'] = len(self.running_competiitions)
        basic_info['ultima atualizacao'] = self.details['ultima atualizacao']

        return basic_info

    def main_data(self):
        other_info = {
            'tecnico': self.coach,
            'jogadores': self.squad,
            'outros membros': self.staff,
            'competicoes': self.running_competiitions,
            'confrontos': self.matches,
            'detalhes': self.details.copy()
        }

        return other_info

    def activate_matches(self):
        page_search = 'matches'
        option_dict = self._access_internal_option(page_search)

        matchday_dict = dict()
        for i in option_dict[page_search]:
            for j in i:
                if j == 'matchday':
                    matchday_dict[i[j]] = list()

        for i in option_dict[page_search]:
            for j in matchday_dict:
                if j == i['matchday']:
                    match = {i['id']: i}
                    matchday_dict[j].append(match)

        self.matches = matchday_dict

    def _access_internal_option(self, page_search):
        access = ApiAccess(Team.options, page_search, self.__code_id)
        accessed_dict = access.open_required_dict()

        return accessed_dict

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
