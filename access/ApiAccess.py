import json
import requests


def _write_page_address(resources_tuple: tuple, page_search='all', code_id=''):
    sub_resources_menu = dict()

    resource_type = resources_tuple[0]
    resources_list = resources_tuple[1]

    for i in resources_list:
        if i == 'all':
            string_address = f'{code_id}'
        elif i == 'particular':
            string_address = f'{code_id}'
        else:
            string_address = f'{code_id}/{i}'
        sub_resources_menu[i] = string_address

    address = f'/{resource_type}/{sub_resources_menu[page_search]}'

    return address


class ApiAccess:

    def __init__(self):

        self.__api_page = 'https://api.football-data.org/v4/'
        self.__my_key_token = {'X-Auth-Token': 'f6d47b2ad83145d09dfde55a98a40087'}

    def open_resource_info(self, resource_menu: tuple, page_search: str = None, code_id: str = None):
        if page_search is None and code_id is None:
            address = _write_page_address(resource_menu)
        else:
            page_address = _write_page_address(resource_menu, page_search, code_id)
            address = page_address

        dict_to_show = self._make_request(address)

        return dict_to_show

    def all_areas_dict_with_not_allowed(self):
        all_areas = dict()

        area_page = 'areas/'
        areas_from_source = self._make_request(area_page)

        for i in areas_from_source['areas']:
            all_areas[i['name']] = i

        return all_areas

    def all_competitions_with_not_allowed_dict(self):
        all_competitions = dict()

        page_name = 'competitions/'
        dict_from_source = self._make_request(page_name)

        for i in dict_from_source['competitions']:
            all_competitions[i['name']] = i

        return all_competitions

    def all_matches_with_not_allowed_dict(self):
        all_matches = dict()

        page_name = 'matches/'
        dict_from_source = self._make_request(page_name)

        for i in dict_from_source['matches']:
            all_matches[i['id']] = i

        return all_matches

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

    @property
    def api_page(self):
        return self.__api_page
