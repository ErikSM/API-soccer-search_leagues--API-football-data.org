from access.ApiAccess import ApiAccess
from structure import Team
from structure.Match import Match


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

        self.__code_id = self.__details['id']
        self.__name = self.__details['name']
        self.__acronym = self.__details['code']
        self.__type = self.__details['type']

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
        try:
            option_dict[page_search]
        except Exception as ex:
            self.standings = {'Inexistente': ('Error', f'Nao encontrado{ex}')}
        else:

            if len(option_dict[page_search]) > 1:
                self.standings = dict()

                for i in option_dict[page_search]:
                    group_standings = []

                    table = i['table']
                    for j in table:
                        group_standings.append((j['position'], j['team']['name']))
                    group_name = (i['group'])

                    self.standings[group_name] = group_standings

            elif len(option_dict[page_search]) == 1:
                self.standings = {i['position']: i['team']['name']
                                  for i in option_dict[page_search][0]['table']}

    def activate_matches(self):
        page_search = 'matches'
        option_dict = self._access_internal_option(page_search)

        matchdays = set()
        for i in option_dict[page_search]:
            matchdays.add(i['matchday'])

        matches = dict()
        for i in matchdays:
            key = f"{i}a Rodada"
            matches[key] = list()

        for i in option_dict[page_search]:
            for z in matches:
                if f"{i['matchday']}a Rodada" == z:
                    matches[z].append(Match(i))

        self.matches = matches

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

        basic_info['competicao'] = self.__details['name']
        basic_info['sigla'] = self.__details['code']
        basic_info['temporada atual'] = f"{self.__details['seasons'][0]['startDate']} / " \
                                        f"{self.__details['seasons'][0]['startDate']}"
        basic_info['atualizado em'] = self.__details['lastUpdated']

        return basic_info

    def get_details(self):
        details_copy = self.__details.copy()

        return details_copy

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    @property
    def type(self):
        return self.__type
