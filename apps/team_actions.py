from tkinter import ANCHOR, END

from apps.AppMain import AppMain
from structure.Team import Team


def select_team(self: AppMain, from_menu=False):
    selected_team = self.list_options.get(ANCHOR)

    try:
        if from_menu:
            code_index = selected_team.index('-')
            team_code = selected_team[:code_index]

            self.team = Team(team_code)
        else:
            self.team = self.competition.teams[selected_team]

        self.clear_all()
        self.entry_title.insert(END, self.team.name)

        all_data = self.team.main_data()
        for i in all_data:
            self.list_options.insert(END, i)

        basic_info = self.team.basic_information()
        for i in basic_info:
            string = '{}: {}'.format(i, basic_info[i])
            self.text_place.insert(END, f'\n{string}\n')

    except Exception as ex:
        self.error_messege(ex)
    else:
        self.setting_button_to(lambda: select_team_option(self))


def select_team_option(self: AppMain):
    selected = self.list_options.get(ANCHOR)

    if selected == 'jogadores':
        self.clear_all()
        self.setting_button_to(None)

        self.entry_title.insert(END, f"{self.team.name}: (Jogadores)")

        all_players = self.team.squad
        for i in all_players:
            self.list_options.insert(1, i)

    elif selected == 'competicoes':
        self.clear_all()
        self.setting_button_to(None)

        self.entry_title.insert(END, f"{self.team.name}: (Competicoes)")

        all_competitions = self.team.competiitions
        for i in all_competitions:
            self.list_options.insert(END, i)

    elif selected == 'confrontos':
        self.clear_all()
        self.setting_button_to(None)

        self.entry_title.insert(END, f"{self.team.name}: (Confrontos)")

        self.team.activate_matches()
        all_matches = self.team.matches
        for i in all_matches:
            for j in all_matches[i]:
                self.list_options.insert(END, f"{all_matches[i][j].resume}")

    elif selected == 'sobre o clube':
        self.clear_all()
        self.setting_button_to(None)

        self.entry_title.insert(END, f"{self.team.name}: (Sobre o clube)")

        all_about = self.team.about
        for i in all_about:
            self.list_options.insert(END, f"{i}:   {all_about[i]}")

        basic_info = self.team.basic_information()
        for i in basic_info:
            string = '{}: {}'.format(i, basic_info[i])
            self.text_place.insert(END, f'\n{string}\n')
