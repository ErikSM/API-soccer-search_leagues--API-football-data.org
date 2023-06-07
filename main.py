import json
import requests

# documentation_source_page_adress = "https://www.football-data.org/documentation/quickstart"

collections_source_adress = 'https://www.postman.com/collections/f3449621c47b66b53725'

api_permitions_acount = ['12 competitions',
                         'Scores delayed',
                         'Fixtures, Schedules',
                         'League Tables']

allowed_competitions = {'WC': 'FIFA World Cup', 'CL': 'UEFA Champions League',
                        'BL1': 'Bundesliga', 'DED': 'Eredivisie',
                        'BSA': 'Campeonato Brasileiro Série A',
                        'PD': 'Primera Division', 'FL1': 'Ligue 1',
                        'ELC': 'Championship', 'PPL': 'Primeira Liga',
                        'EC': 'European Championship', 'SA': 'Serie A',
                        'PL': 'Premier League', 'CLI': 'Copa Libertadores'}

api_page = 'https://api.football-data.org/v4/'
my_key_token = {'X-Auth-Token': 'f6d47b2ad83145d09dfde55a98a40087'}


def create_file_request(adress, need_key=True):
    adress_body = api_page
    request = None

    if need_key:

        headers = my_key_token
        request = requests.get(f'{adress_body}{adress}', headers=headers)

    elif not need_key:

        request = requests.get(f'{adress_body}{adress}')
        print(f'{adress_body}{adress}')
    file = json.loads(request.text)

    return file


def show_my_allowed_competitions():
    for i in allowed_competitions:
        print(i)
        print(allowed_competitions[i])


def show_my_permitions_acount():
    for i in api_permitions_acount:
        print(i)


def show_all_items_from_collections_source(item_to_show='all'):
    request = requests.get(f'{collections_source_adress}')
    collections = json.loads(request.text)

    if item_to_show == 'all':
        for i in collections:
            print(i)
            print(collections[i])
    else:
        for i in collections[item_to_show]:
            print('-' * 300)
            print(f"\n*** {i['name']}:")
            for j in i:
                print(f'{j}: {type(i[j])} \n-> {i[j]}\n')


show_all_items_from_collections_source('item')