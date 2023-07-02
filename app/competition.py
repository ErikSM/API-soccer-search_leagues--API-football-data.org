from tkinter import ANCHOR, END

from access.info_api import names_allowed_leagues, translator_pt_br
from app.AppMain import AppMain
from app.team import select_team
from structure.Competition import Competition
from structure.Team import Team


def select_competition(self: AppMain, from_return=False):
    self.setting_button_to(lambda: select_competition_option(self))
    self.setting_return_button_to(self.clear_all)

    if not from_return:
        competition_selected = self.list_options.get(ANCHOR)
        league_code = names_allowed_leagues[competition_selected]

        competition = Competition(league_code)
        self.competition = competition
    else:
        competition = Competition
        self.competition = self.competition

    self.clear_all()

    self.entry_title.insert(END, self.competition.name)

    all_options = competition.pages_list
    for i in all_options:
        if i == 'all' or i == 'particular':
            pass
        else:
            self.list_options.insert(END, translator_pt_br(i))

    basic_info = self.competition.basic_information()
    for i in basic_info:
        string = '{}: {}'.format(i, basic_info[i])
        self.text_place.insert(END, f'\n{string}\n')


def select_competition_option(self: AppMain):
    selected = self.list_options.get(ANCHOR)
    self.setting_return_button_to(lambda: select_competition(self, True))

    if selected == 'equipes':
        self.clear_all()
        self.setting_button_to(lambda: select_team(self, 'teams'))

        self.entry_title.insert(END, f"{self.competition.name}: (Equipes)")

        self.competition.activate_teams(Team)
        all_teams = self.competition.teams
        for i in all_teams:
            self.list_options.insert(END, i)

    elif selected == 'classificacao':
        self.clear_all()
        self.setting_button_to(lambda: select_team(self, 'standings'))

        self.entry_title.insert(END, f"{self.competition.name}: (Classificacao)")

        self.competition.activate_standings()
        standings = self.competition.standings
        if self.competition.type == 'CUP':
            for i in standings:
                self.list_options.insert(END, i)
                for j in standings[i]:
                    string = '{}- {}'.format(j[0], j[1])
                    self.list_options.insert(END, string)
                self.list_options.insert(END, '')
        else:
            for i in standings:
                string = '{}- {}'.format(i, standings[i])
                self.list_options.insert(END, string)

    elif selected == 'confrontos':
        self.clear_all()
        self.setting_button_to(lambda: select_competiton_matchday(self))

        self.entry_title.insert(END, f"{self.competition.name}: (Rodadas)")

        try:
            self.competition.activate_matches()
            all_matches = self.competition.matches
            for i in all_matches:
                self.list_options.insert(END, f"{i}")
        except Exception as ex:
            self.list_options.insert(END, f"Error {ex}")

    elif selected == 'artilharia':
        self.clear_all()
        self.setting_button_to(lambda: select_competition_scorer(self, all_scorers))

        self.entry_title.insert(END, f"{self.competition.name}: (Artilharia)")
        self.competition.activate_scorers()

        all_scorers = self.competition.scorers
        for i in all_scorers:
            code_id = self.competition.scorers[i]['player']['id']
            player = self.competition.scorers[i]['player']['name']
            goals = self.competition.scorers[i]['goals']
            self.list_options.insert(1, "{}-{}:     {} gols".format(code_id, player, goals))

    else:
        self.text_place.delete(1.0, END)

    basic_info = self.competition.basic_information()
    for i in basic_info:
        string = '{}: {}'.format(i, basic_info[i])
        self.text_place.insert(END, f'\n{string}\n')


def select_competition_scorer(self: AppMain, scorers_dict: dict):
    scorer_selected = self.list_options.get(ANCHOR)

    index_one = scorer_selected.index('-')
    index_two = scorer_selected.index(':')
    scorer_name = scorer_selected[index_one + 1: index_two]

    self.clear_only('text')

    scorer_info = scorers_dict[scorer_name]
    for i in scorer_info:
        if i == 'team' or i == 'player':
            info = scorer_info[i]['name']
        else:
            info = scorer_info[i]
        string = '{}: {}'.format(i, info)
        self.text_place.insert(END, f'\n{string}\n')


def select_competiton_matchday(self: AppMain):
    matchday_selected = self.list_options.get(ANCHOR)
    self.setting_button_to(lambda: show_match_details(self, matches_dict))

    self.clear_all()

    self.entry_title.insert(END, f"{self.competition.name}: ({matchday_selected})")

    matches_dict = dict()
    all_matches = self.competition.matches[matchday_selected]
    for i in all_matches:
        matches_dict[i.resume] = i
        self.list_options.insert(END, i.resume)


def show_match_details(self: AppMain, matches_dict: dict):
    match_selected = self.list_options.get(ANCHOR)

    self.clear_only('text')
    self.clear_only('entry')
    self.entry_title.insert(END, f"{self.competition.name}: ({match_selected})")

    match = matches_dict[match_selected]
    self.match = match

    basic_info = self.match.basic_information()
    for i in basic_info:
        string = '{}: {}'.format(i, basic_info[i])
        self.text_place.insert(END, f'\n{string}\n')
