from tkinter import ANCHOR, END

from app.AppMain import AppMain
from structure.Person import Person


def select_person(self: AppMain, from_to):
    selected_person = self.list_options.get(ANCHOR)

    self.clear_only('text')

    if from_to == 'scorers':
        index_one = selected_person.index('-')
        index_two = selected_person.index(':')
        scorer_name = selected_person[index_one + 1: index_two]

        self.person = self.competition.scorers[scorer_name]

    elif from_to == 'team':
        person = self.team.squad[selected_person]
        self.person = person

    else:
        code_index = selected_person.index('-')
        person_code = selected_person[:code_index]

        person = Person(person_code)
        self.person = person

    if from_to == 'scorers':
        basic_info = self.person

        for i in basic_info:
            if i == 'team' or i == 'player':
                info = basic_info[i]['name']
            else:
                info = basic_info[i]
            string = '{}: {}'.format(i, info)
            self.text_place.insert(END, f'\n{string}\n')
    else:
        basic_info = self.person.basic_information()
        for i in basic_info:
            string = '{}: {}'.format(i, basic_info[i])
            self.text_place.insert(END, f'\n{string}\n')
