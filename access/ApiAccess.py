import json
import requests


class ApiAccess:

    def __init__(self, resource_options: tuple, page_search='all', code_id=''):

        self.__resource_menu = resource_options
        self.__page_search = page_search
        self.__code_id = code_id

        self.__my_key_token = {'X-Auth-Token': 'f6d47b2ad83145d09dfde55a98a40087'}
        self.__api_page = 'https://api.football-data.org/v4/'

    @property
    def api_page(self):
        return self.__api_page

    def open_required_dict(self):
        address = self._write_page_address()
        dict_required = self._make_request(address)

        return dict_required

    def _write_page_address(self, ):
        sub_resources_menu = dict()

        resource_type = self.__resource_menu[0]
        resources_list = self.__resource_menu[1]

        for i in resources_list:
            if i == 'all':
                string_address = f'{self.__code_id}'
            elif i == 'particular':
                string_address = f'{self.__code_id}'
            else:
                string_address = f'{self.__code_id}/{i}'
            sub_resources_menu[i] = string_address

        address = f'/{resource_type}/{sub_resources_menu[self.__page_search]}'

        return address

    def _make_request(self, address: str, need_key=True):
        address_body = self.__api_page
        request = None

        if need_key:
            headers = self.__my_key_token
            request = requests.get(f'{address_body}{address}', headers=headers)

        elif not need_key:
            request = requests.get(f'{address_body}{address}')

        captured_dict = json.loads(request.text)

        return captured_dict
