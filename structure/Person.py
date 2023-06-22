from datetime import datetime

from access.ApiAccess import ApiAccess


def access_person_dict(person_code):
    access = ApiAccess(Person.options, 'particular', person_code)
    person_dict = access.open_required_dict()

    return person_dict


class Person:
    pages_list = ['particular', 'matches']
    options = ('persons', pages_list)

    def __init__(self, data_dict_or_data_code):

        if type(data_dict_or_data_code) == dict:
            self.__details = data_dict_or_data_code
        elif type(data_dict_or_data_code) == str:
            self.__details = access_person_dict(data_dict_or_data_code)

        self.__code_id = self.__details['id']
        self.__name = self.__details['name']
        self.__position = self.__details['position']
        self.__birthday = self.__details['dateOfBirth']
        self.__nationality = self.__details['nationality']

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    def basic_information(self):
        basic_info = dict()
        basic_info['nome'] = self.__name
        basic_info['posicao'] = self.__position
        basic_info['idade'] = (int(self.__birthday[:4]) - int(datetime.today().year))
        basic_info['nacionalidade'] = self.__details['nationality']

        return basic_info
