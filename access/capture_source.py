import json
import requests


api_page = 'https://api.football-data.org/v4/'
my_key_token = {'X-Auth-Token': 'f6d47b2ad83145d09dfde55a98a40087'}


def create_file_request(address: str, need_key=True):
    address_body = api_page
    request = None

    if need_key:

        headers = my_key_token
        request = requests.get(f'{address_body}{address}', headers=headers)

    elif not need_key:

        request = requests.get(f'{address_body}{address}')
        print(f'{address_body}{address}')
    file = json.loads(request.text)

    return file


def write_sub_resource_page_address(resources_tuple: tuple, page_search='all', code_id=''):
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

    print(address)

    return address
