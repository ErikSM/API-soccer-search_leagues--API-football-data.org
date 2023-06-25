from tkinter import Menu, END

from access.ApiAccess import ApiAccess
from access.info_api import names_allowed_leagues
from apps.AppMain import AppMain
from apps.competition_actions import select_competition
from apps.team_actions import select_team
from structure.Team import Team


def create_menu(self: AppMain):
    self.menu = Menu(self.window)
    self.window.config(menu=self.menu)

    self.menu_file = Menu(self.menu, tearoff=0)
    self.menu.add_cascade(label='file', menu=self.menu_file)
    self.menu_file.add_command(label='New', command=lambda: open_menu_competitions(self))

    self.menu.add_command(label='competitions', command=lambda: open_menu_competitions(self))

    self.menu.add_command(label='teams', command=lambda: open_menu_teams(self))


def open_menu_competitions(self: AppMain):
    self.setting_button_to(lambda: select_competition(self))

    self.clear_all()

    self.entry_title.insert(END, 'Todas as competicoes:')
    for i in names_allowed_leagues:
        self.list_options.insert(END, i)


def open_menu_teams(self: AppMain):
    self.setting_button_to(lambda: select_team(self, True))

    team_access = ApiAccess(Team.options)
    team_all = team_access.open_required_dict()

    self.clear_all()

    self.entry_title.insert(END, 'Todos os times:')
    for i in team_all['teams']:
        self.list_options.insert(END, f"{i['id']}- {i['name']}")
