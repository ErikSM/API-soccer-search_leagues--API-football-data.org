from access.ApiAccess import ApiAccess
from structure import Team


def access_competition_dict(league_code):
    access = ApiAccess(Competition.options, 'particular', league_code)
    competition_dict = access.open_required_dict()

    return competition_dict


class Competition:
    pages_list = ['all', 'particular', 'standings', 'matches', 'teams', 'scorers']
    options = ('competitions', pages_list)

    all_competitions = ApiAccess(options)

    def __init__(self, league_code):

        self.__details = access_competition_dict(league_code)

        self.__name = self.__details['name']
        self.__code_id = self.__details['id']
        self.__acronym = self.__details['code']

        self.teams = None
        self.standings = None
        self.matches = None
        self.scorers = None

    def activate_teams(self, team: Team):
        page_search = 'teams'
        option_dict = self._access_internal_option(page_search)
        self.teams = {i['name']: team(i)
                      for i in option_dict[page_search]}

    def activate_standings(self):
        page_search = 'standings'
        option_dict = self._access_internal_option(page_search)
        self.standings = {i['position']: i['team']['name']
                          for i in option_dict[page_search][0]['table']}

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

    def activate_scorers(self):
        page_search = 'scorers'
        option_dict = self._access_internal_option(page_search)
        self.scorers = {i['player']['name']: i for i in option_dict[page_search]}

    def _access_internal_option(self, page_search):
        access = ApiAccess(Competition.options, page_search, self.__acronym)
        accessed_dict = access.open_required_dict()

        return accessed_dict

    def basic_information(self):
        basic_info = dict()

        basic_info['nome'] = self.__details['name']
        basic_info['sigla'] = self.__details['code']
        basic_info['temporada atual'] = f"{self.__details['seasons'][0]['startDate']} / " \
                                        f"{self.__details['seasons'][0]['startDate']}"
        basic_info['atualizado em'] = self.__details['lastUpdated']

        return basic_info

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    @property
    def details(self):
        return self.__details
