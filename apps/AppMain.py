from tkinter import *
from access.menus import *

from access.ApiAccess import ApiAccess
from access.info_api import names_allowed_leagues
from structure.Competition import Competition
from structure.Team import Team


def start():
    AppMain()


class AppMain:

    def __init__(self):

        self.title = 'Soccer Search League'

        self.competition = None
        self.team = None

        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry("700x500+400+100")
        self.window.resizable(False, False)
        self.window.config(bg='#365949')

        self.img_address = PhotoImage(file='assets/emblem_xx.png')

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        self.menu_file = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='file', menu=self.menu_file)
        self.menu_file.add_command(label='New', command=self.initial_setting)

        self.menu.add_command(label='competitions', command=self.open_menu_competitions)

        self.menu.add_command(label='teams', command=self.open_menu_teams)

        self.frame_up = Frame(self.window, height=2, bg='black')
        self.frame_up.pack(fill=X)
        self.frame_central = Frame(self.window, bg='#162E23')
        self.frame_central.pack()
        self.frame_down = Frame(self.window, height=2, bg='black')
        self.frame_down.pack(fill=X)

        self.label_up = Label(self.frame_up, font=("Times", "24", "bold italic"), bg='#3B4641', fg='black')
        self.label_up.config(text='Soccer League Search App')
        self.label_up.pack(fill=X)
        self.label_down = Label(self.frame_down, font=("'Helvetica", "16", "italic"), bg='#3B4641', fg='black')
        self.label_down.config(text='Choose the league and find your favorite team...')
        self.label_down.pack(fill=X)

        self.sub_frame_left = Frame(self.frame_central, bg='#162E23')
        self.sub_frame_left.grid(row=0, column=0, columnspan=1)
        self.sub_frame_right = Frame(self.frame_central, bg='#162E23')
        self.sub_frame_right.grid(row=0, column=1, columnspan=2)

        self.entry_title = Entry(self.sub_frame_left, bg='black', fg='white', width=48, bd=10)
        self.entry_title.grid(row=0, column=0)
        self.list_options = Listbox(self.sub_frame_left, bg='black', fg='white', height=22, width=48, bd=10)
        self.list_options.grid(row=1, column=0)

        y_axis = Scrollbar(self.sub_frame_left, orient=VERTICAL, command=self.list_options.yview)
        y_axis.grid(row=1, rowspan=22, column=1, sticky=N + S)
        self.list_options.config(yscrollcommand=y_axis.set)

        self.butt_frame = Frame(self.sub_frame_right, bg='#162E23')
        self.butt_frame.grid(row=10, column=1)
        self.img_label = Label(self.sub_frame_right, image=self.img_address, bd=15, bg='black')
        self.img_label.grid(row=10, column=45)
        self.text_place = Text(self.sub_frame_right, bg='black', fg='white', bd=15, height=17, width=50)
        self.text_place.grid(row=21, rowspan=40, column=0, columnspan=100)

        self.button_select = Button(self.butt_frame)
        self.button_return = Button(self.butt_frame)

        self.initial_setting()

        self.window.mainloop()

    def open_menu_competitions(self):
        self._setting_button_to('competition')

        self._clear_all()

        self.entry_title.insert(END, 'Todas as competicoes:')
        for i in names_allowed_leagues:
            self.list_options.insert(END, i)

    def open_menu_teams(self):
        self._setting_button_to('team_from_menu')

        team_access = ApiAccess(Team.options)
        team_all = team_access.open_required_dict()

        self._clear_all()

        self.entry_title.insert(END, 'Todos os times:')
        for i in team_all['teams']:
            self.list_options.insert(END, f"{i['id']}- {i['name']}")

    def select_competition(self):
        self._setting_button_to('option')

        competition_selected = self.list_options.get(ANCHOR)
        league_code = names_allowed_leagues[competition_selected]

        competition = Competition(league_code)
        self.competition = competition

        self._clear_all()

        self.entry_title.insert(END, self.competition.name)

        for i in competition.pages_list:
            self.list_options.insert(END, i)

        basic_info = self.competition.basic_information()
        for i in basic_info:
            string = '{}: {}'.format(i, basic_info[i])
            self.text_place.insert(END, f'\n{string}\n')

    def select_option(self):

        selected = self.list_options.get(ANCHOR)

        self._clear_all()
        self._setting_button_to('team')

        if selected == 'teams':
            self.entry_title.insert(END, f"{self.competition.name}: (Equipes)")

            self.competition.activate_teams()

            for i in self.competition.teams:
                self.list_options.insert(END, i)

        elif selected == 'standings':
            self.entry_title.insert(END, f"{self.competition.name}: (Classificacao)")

            self.competition.activate_standings()

            for i in self.competition.standings:
                string = '{}- {}'.format(i, self.competition.standings[i])
                self.list_options.insert(END, string)

        elif selected == 'matches':
            self.entry_title.insert(END, f"{self.competition.name}: (Rodadas)")

            self.competition.activate_matches()

            for i in self.competition.matches:
                self.list_options.insert(END, f"{i}a. Rodada")

        elif selected == 'scorers':
            self.entry_title.insert(END, f"{self.competition.name}: (Estatisticas)")

            self.competition.activate_scorers()

            for i in self.competition.scorers:
                print(i)

        basic_info = self.competition.basic_information()
        for i in basic_info:
            string = '{}: {}'.format(i, basic_info[i])
            self.text_place.insert(END, f'\n{string}\n')

    def select_team(self, from_menu=False):
        self._setting_button_to('xxx')

        selected_team = self.list_options.get(ANCHOR)

        if from_menu:
            code_index = selected_team.index('-')
            team_particular = ApiAccess(Team.options, 'particular', selected_team[:code_index])

            self.team = Team(team_particular.open_required_dict())
        else:
            self.team = self.competition.teams[selected_team]

        self._clear_all()
        name = self.team.name
        self.entry_title.insert(END, name)

        all_data = self.team.main_data()
        for i in all_data:
            self.list_options.insert(END, i)

        basic_info = self.team.basic_information()
        for i in basic_info:
            string = '{}: {}'.format(i, basic_info[i])
            self.text_place.insert(END, f'\n{string}\n')

    def initial_setting(self):
        self.open_menu_competitions()

    def _clear_all(self):
        self.entry_title.delete(0, END)
        self.list_options.delete(0, END)
        self.text_place.delete(1.0, END)

    def _setting_button_to(self, config):
        self.button_select.destroy()
        self.button_return.destroy()

        self.button_select = Button(self.butt_frame, bg='#3B4641', fg='white', bd=1, width=5)
        self.button_select.grid(row=0, column=0)

        self.button_return = Button(self.butt_frame, bg='#3B4641', fg='white', bd=1, width=5)
        self.button_return.grid(row=1, column=0)
        self.button_return.config(text='return', command=self.initial_setting)

        if config == 'competition':
            self.button_select.config(text='select', command=self.select_competition)

        elif config == 'team':
            self.button_select.config(text='select', command=self.select_team)

        elif config == 'team_from_menu':
            self.button_select.config(text='select', command=lambda: self.select_team(True))

        elif config == 'option':
            self.button_select.config(text='select', command=self.select_option)

        else:
            self.button_select.config(text='select', command=None)
