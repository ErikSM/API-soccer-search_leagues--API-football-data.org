from tkinter import ANCHOR, END

from access.info_api import names_allowed_leagues
from access.menus import translator_pt_br
from apps.AppMain import AppMain
from apps.team_actions import select_team
from structure.Competition import Competition
from structure.Team import Team


def select_competition(self: AppMain):
    self.setting_button_to(lambda: select_competition_option(self))

    competition_selected = self.list_options.get(ANCHOR)
    league_code = names_allowed_leagues[competition_selected]

    competition = Competition(league_code)
    self.competition = competition

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

    if selected == 'equipes':
        self.clear_all()
        self.setting_button_to(lambda: select_team(self))

        self.entry_title.insert(END, f"{self.competition.name}: (Equipes)")

        self.competition.activate_teams(Team)
        all_teams = self.competition.teams
        for i in all_teams:
            self.list_options.insert(END, i)

    elif selected == 'classificacao':
        self.clear_all()
        self.setting_button_to(lambda: select_team(self))

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
        self.setting_button_to(None)

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
        self.setting_button_to(None)

        self.entry_title.insert(END, f"{self.competition.name}: (Artilharia)")
        self.competition.activate_scorers()

        for i in self.competition.scorers:
            code_id = self.competition.scorers[i]['player']['id']
            player = self.competition.scorers[i]['player']['name']
            goals = self.competition.scorers[i]['goals']
            self.list_options.insert(1, "({}) {}:     {} gols".format(code_id, player, goals))

    else:
        self.text_place.delete(1.0, END)

    basic_info = self.competition.basic_information()
    for i in basic_info:
        string = '{}: {}'.format(i, basic_info[i])
        self.text_place.insert(END, f'\n{string}\n')
