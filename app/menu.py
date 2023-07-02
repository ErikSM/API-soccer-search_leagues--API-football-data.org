from tkinter import Menu

from access.ApiAccess import ApiAccess
from app.AppMain import AppMain
from app.competition import select_competition
from app.team import select_team
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

    self.print_competitions_allowed()


def open_menu_teams(self: AppMain):
    self.setting_button_to(lambda: select_team(self, 'menu'))

    team_access = ApiAccess(Team.options)
    team_all = team_access.open_required_dict()

    self.print_teams_allowed(team_all)
