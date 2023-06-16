from structure import Team


class Competition:

    def __init__(self, competition: dict, team: Team):
        self.__count = competition['count']
        self.__season = competition['filters']['season']

        self.__info_about = competition['competition']
        self.__season_details = competition['season']

        self.__teams = {i['name']: team(i) for i in competition['teams']}

    def basic_information_pt_br(self):
        basic_info = dict()

        basic_info['id'] = self.__info_about['id']
        basic_info['sigla'] = self.__info_about['code']
        basic_info['nome'] = self.__info_about['name']
        basic_info['temporada'] = self.__season
        basic_info['total de equipes'] = self.__count
        basic_info['rodada atual'] = self.__season_details['currentMatchday']

        return basic_info

    def get_season_period(self):
        start = self.__season_details['startDate']
        end = self.__season_details['endDate']

        dates = f'{start}/{end}'
        pt_br = 'Periodo'

        period_date = (pt_br, dates)

        return period_date

    def get_current_matchday(self):
        number = self.__season_details['currentMatchday']
        pt_br = 'Rodada atual'

        match_day = (pt_br, number)

        return match_day

    def get_winner(self):
        team = self.__season_details['winner']
        pt_br = 'Vencedor'

        winner = (pt_br, team)

        return winner

    def get_name(self):
        return self.__info_about['name']

    def get_id(self):
        return self.__info_about['id']

    def get_allowed(self):
        return self.__info_about['code']

    @property
    def count(self):
        return self.__count

    @property
    def season(self):
        return self.__season

    @property
    def info_about(self):
        return self.__info_about

    @property
    def season_detais(self):
        return self.__season_details

    @property
    def teams(self):
        return self.__teams
