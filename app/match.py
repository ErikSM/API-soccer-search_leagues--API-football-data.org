from tkinter import ANCHOR, END

from app.AppMain import AppMain


def select_competiton_matchday(self: AppMain):
    matchday_selected = self.list_options.get(ANCHOR)
    self.setting_button_to(lambda: show_match_details(self, 'competition', matches_dict))

    self.clear_all()

    self.entry_title.insert(END, f"{self.competition.name}: ({matchday_selected})")

    matches_dict = dict()
    all_matches = self.competition.matches[matchday_selected]
    for i in all_matches:
        matches_dict[i.resume] = i
        self.list_options.insert(END, i.resume)


def show_match_details(self: AppMain, from_to, matches_dict: dict = None):
    match_selected = self.list_options.get(ANCHOR)

    self.clear_only('text')
    self.clear_only('entry')

    if from_to == 'competition':
        self.entry_title.insert(END, f"{self.competition.name}: ({match_selected})")
    elif from_to == 'team':
        self.entry_title.insert(END, f"{self.team.name}: ({match_selected})")

    match = matches_dict[match_selected]
    self.match = match

    basic_info = self.match.basic_information()
    for i in basic_info:
        string = '{}: {}'.format(i, basic_info[i])
        self.text_place.insert(END, f'\n{string}\n')
