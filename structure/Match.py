from access.ApiAccess import ApiAccess


def access_match_dict(team_code):
    access = ApiAccess(Match.options, 'particular', team_code)
    team_dict = access.open_required_dict()

    return team_dict


class Match:
    pages_list = ['all', 'particular', 'head2head']
    options = ('matches', pages_list)

    def __init__(self, data_dict_or_data_code):

        self.__detais = dict or str
        if type(data_dict_or_data_code) is dict:
            self.__details = data_dict_or_data_code
        elif type(data_dict_or_data_code) is str:
            self.__details = access_match_dict(data_dict_or_data_code)

        self.__code_id = self.__details['id']
        self.__matchday = self.__details['matchday']

        self.__home_team = self.__detais['homeTeam']
        self.__away_team = self.__detais['awayTeam']

        self.about = {
            "area": self.__details['area'],
            "competition": self.__details['competition'],
            "season": self.__details['season'],
            "group": self.__details['group'],
            "utc_date": self.__details['utcDate'],
            "status": self.__details['status'],
            "stage": self.__details['stage'],
            "last_updated": self.__details['lastUpdated'],
            "odds": self.__details['odds'],
            "referees": self.__details['referees'],
            "score": self.__details['score'],
            "winner": self.__details['score']['winner']
        }

        if self.about['winner'] is None:
            home, away = '-', '-'
        else:
            home = self.about['score']['fullTime']['home']
            away = self.about['score']['fullTime']['away']

        self.resume = "{}({})x({}){}".format(self.__details['homeTeam']['tla'],
                                             home, away,
                                             self.__details['awayTeam']['tla'])

    def basic_information(self):
        basic_info = {
            'competicao': self.about['competition']['name'],
            'temporada': self.about['season']['startDate'][:4],
            'rodada': self.__matchday,
            'placar': self.resume,
            'anfitriao': self.__details['homeTeam']['name'],
            'visitante': self.__details['awayTeam']['name'],
        }

        return basic_info

    @property
    def code_id(self):
        return self.__code_id

    @property
    def matchday(self):
        return self.__matchday

    @property
    def home_team(self):
        return self.__home_team

    @property
    def away_team(self):
        return self.__away_team
