from access.ApiAccess import ApiAccess
from structure.Match import Match
from structure.Person import Person


def access_team_dict(team_code):
    access = ApiAccess(Team.options, 'particular', team_code)
    team_dict = access.open_required_dict()

    return team_dict


class Team:
    pages_list = ['all', 'particular', 'matches']
    options = ('teams', pages_list)

    all_teams = ApiAccess(options)

    def __init__(self, data_dict_or_data_code):

        self.__details = None
        if type(data_dict_or_data_code) is dict:
            self.__details = data_dict_or_data_code
        elif type(data_dict_or_data_code) is str:
            self.__details = access_team_dict(data_dict_or_data_code)

        self.__code_id = self.__details['id']
        self.__name = self.__details['name']
        self.__area = self.__details['area']

        self.about = {
            "nome popular": self.__details['shortName'],
            "sigla": self.__details['tla'],
            "escudo": self.__details['crest'],
            "endereco": self.__details['address'],
            "website": self.__details['website'],
            "fundacao": self.__details['founded'],
            "cores do clube": self.__details['clubColors'],
            "estadio": self.__details['venue'],
            "ultima atualizacao": self.__details['lastUpdated']
        }

        self.coach = self.__details['coach']
        self.staff = self.__details['staff']

        self.squad = {i['name']: Person(i)
                      for i in self.__details['squad']}

        self.competiitions = {i['name']: i
                              for i in self.__details['runningCompetitions']}

        self.matches = None

    def activate_matches(self):
        page_search = 'matches'
        option_dict = self._access_internal_option(page_search)

        matchday_dict = dict()
        for i in option_dict[page_search]:
            for j in i:
                if j == 'matchday':
                    matchday_dict[f"{i[j]}a Rodada"] = None

        for i in option_dict[page_search]:
            for j in matchday_dict:
                if j == f"{i['matchday']}a Rodada":
                    match = {i['id']: Match(i)}
                    matchday_dict[j] = match

        self.matches = matchday_dict
        print(matchday_dict)

    def _access_internal_option(self, page_search):
        access = ApiAccess(Team.options, page_search, self.__code_id)
        accessed_dict = access.open_required_dict()

        return accessed_dict

    def basic_information(self):
        basic_info = {
            'equipe': self.__name,
            'tecnico': self.coach['name'],
            'estadio': self.about['estadio'],
            'Total de competicoes': len(self.competiitions),
            'ultima atualizacao': self.about['ultima atualizacao']
        }

        return basic_info

    def main_data(self):
        main_data = {
            'jogadores': self.squad,
            'competicoes': self.competiitions,
            'confrontos': self.matches,
            'sobre o clube': self.about.copy()
        }

        return main_data

    def get_acronym(self):
        return self.about['sigla']

    def get_details(self):
        details_copy = self.__details.copy

        return details_copy

    @property
    def area(self):
        return self.__area

    @property
    def code_id(self):
        return self.__code_id

    @property
    def name(self):
        return self.__name
