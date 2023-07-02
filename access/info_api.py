import json
import requests

documentation_source_page_address = "https://www.football-data.org/documentation/quickstart"

collections_source_address = 'https://www.postman.com/collections/f3449621c47b66b53725'

api_account_permissions = ['12 competitions',
                           'Scores delayed',
                           'Fixtures, Schedules',
                           'League Tables']

acronyms_allowed_leagues = {'WC': 'FIFA World Cup',
                            'CL': 'UEFA Champions League',
                            'BL1': 'Bundesliga',
                            'DED': 'Eredivisie',
                            'BSA': 'Campeonato Brasileiro Série A',
                            'PD': 'Primera Division',
                            'FL1': 'Ligue 1',
                            'ELC': 'Championship',
                            'PPL': 'Primeira Liga',
                            'EC': 'European Championship',
                            'SA': 'Serie A',
                            'PL': 'Premier League',
                            'CLI': 'Copa Libertadores'}

names_allowed_leagues = {acronyms_allowed_leagues[i]: i
                         for i in acronyms_allowed_leagues}


def translator_pt_br(string):
    translate = {
        'all': 'todos',
        'particular': 'particular',
        'standings': 'classificacao',
        'matches': 'confrontos',
        'teams': 'equipes',
        'scorers': 'artilharia',
        'head2head': 'time Vs time'
    }

    return translate[string]


def show_my_allowed_competitions():
    for i in acronyms_allowed_leagues:
        print(i)
        print(acronyms_allowed_leagues[i])


def show_my_account_permissions():
    for i in api_account_permissions:
        print(i)


def show_all_items_from_collections_source(item_to_show='all'):
    request = requests.get(f'{collections_source_address}')
    collections = json.loads(request.text)

    if item_to_show == 'all':

        for i in collections:
            print(i)
            print(collections[i])

    elif item_to_show == 'auth' or item_to_show == 'info':

        for i in collections[item_to_show]:
            print(i)
            print(collections[item_to_show][i])
            print('-' * 300)

    else:
        for i in collections[item_to_show]:

            print(('-' * 300) + '\n')

            if item_to_show == 'item':
                print(f"***(( {i['name']}:))***\n")

            for j in i:
                print(f'{j}: {type(i[j])} \n'
                      f'-> {i[j]}\n')
