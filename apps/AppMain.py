from tkinter import *

from access.ApiAccess import ApiAccess
from access.info_api import names_allowed_leagues
from access.menus import *
from structure.Competition import Competition
from structure.Team import Team


def start():
    AppMain()


class AppMain:

    def __init__(self):

        self.title = 'Soccer Search League'

        self.competition_open = Competition
        self.team_open = Team

        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry("700x500+400+100")
        self.window.resizable(False, False)
        self.window.config(bg='#365949')

        self.img_address = PhotoImage(file='assets/emblem_xx.png')

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.menu.add_command(label='file', command=self.select_competition)
        self.menu.add_command(label='competitions', command=self.open_menu_competitions)
        self.menu.add_command(label='teams', command=self.open_menu_teams)

        self.frame_up = Frame(self.window, height=2, bg='black')
        self.frame_up.pack(fill=X)
        self.principal_frame = Frame(self.window, bg='#162E23')
        self.principal_frame.pack()
        self.frame_down = Frame(self.window, height=2, bg='black')
        self.frame_down.pack(fill=X)

        self.label_up = Label(self.frame_up, font=("Times", "24", "bold italic"), bg='#3B4641', fg='black')
        self.label_up.config(text='Soccer League Search App')
        self.label_up.pack(fill=X)
        self.label_down = Label(self.frame_down, font=("'Helvetica", "16", "italic"), bg='#3B4641', fg='black')
        self.label_down.config(text='Choose the league and find your favorite team...')
        self.label_down.pack(fill=X)

        self.sub_frame_left = Frame(self.principal_frame, bg='#162E23')
        self.sub_frame_left.grid(row=0, column=0, columnspan=1)
        self.sub_frame_right = Frame(self.principal_frame, bg='#162E23')
        self.sub_frame_right.grid(row=0, column=1, columnspan=2)

        self.entry_title_list = Entry(self.sub_frame_left, bg='black', fg='white', width=50, bd=5)
        self.entry_title_list.grid(row=0,column=0)
        self.list_options = Listbox(self.sub_frame_left, bg='black', fg='white', height=23, width=50, bd=5)
        self.list_options.grid(row=1, column=0)

        self.button_frame = Frame(self.sub_frame_right, bg='#162E23')
        self.button_frame.grid(row=10, column=1)
        self.image_local_label = Label(self.sub_frame_right, image=self.img_address, bd=10, bg='black')
        self.image_local_label.grid(row=10, column=45)
        self.text_information = Text(self.sub_frame_right, bg='black', fg='white', bd=10, height=15, width=50)
        self.text_information.grid(row=21, rowspan=40, column=0, columnspan=100)

        self.button_select = Button(self.button_frame)
        self.button_return = Button(self.button_frame)

        self.open_menu_competitions()
        self.configuration('select', self.select_competition)

        self.window.mainloop()

    def open_menu_competitions(self):
        self.configuration('select', self.select_competition)

        self.clear_all()

        for i in names_allowed_leagues:
            self.list_options.insert(END, i)

    def open_menu_teams(self):
        self.configuration('select', self.select_team)

        team_access = ApiAccess(team_menu)
        team_all = team_access.open_resource_info()

        self.clear_all()

        for i in team_all['teams']:
            self.list_options.insert(END, i['name'])

    def select_competition(self):
        self.configuration('select', self.select_team)

        competition_selected = self.list_options.get(ANCHOR)
        league_code = names_allowed_leagues[competition_selected]

        competition_access = ApiAccess(competition_menu)
        page_teams = competition_access.open_resource_info('teams', league_code)
        self.competition_open = Competition(page_teams, Team)

        self.clear_all()

        all_teams = self.competition_open.teams
        for i in all_teams:
            self.list_options.insert(END, i)

        information = self.competition_open.basic_information_pt_br()
        for i in information:
            string = '{}: {}'.format(i, information[i])
            self.text_information.insert(END, f'\n{string}\n')

    def select_team(self):
        self.configuration("--", None)

        team_selected = self.list_options.get(ANCHOR)
        self.team_open = self.competition_open.teams[team_selected]

        self.clear_all()

        for i in self.team_open.details:
            self.text_information.insert(END, f'{i}: {self.team_open.details[i]}\n')

        for i in self.team_open.rh:
            try:
                self.list_options.insert(END, f'{i}')
                print(i)
                print(self.team_open.rh[i])
            except KeyError:
                continue

    def clear_all(self):
        self.list_options.delete(0, END)
        self.text_information.delete(1.0, END)

    def configuration(self, text, command):
        self.button_select.destroy()
        self.button_return.destroy()

        self.button_select = Button(self.button_frame, text=text, command=command)
        self.button_select.grid(row=0, column=0)
        self.button_return = Button(self.button_frame, text='return', command=self.clear_all)
        self.button_return.grid(row=1, column=0)
