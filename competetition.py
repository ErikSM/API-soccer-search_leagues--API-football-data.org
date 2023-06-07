from main import create_file_request


def create_all_competitions_dict():
    all_competitions = dict()

    page_name = 'competitions/'
    dict_from_source = create_file_request(page_name)

    for item in dict_from_source['competitions']:
        all_competitions[item['name']] = item

    return all_competitions


def print_all_competitions_allowed(all_competitions: dict):
    for i in all_competitions:
        print(i)
        print(all_competitions[i])


def write_competition_page_adress(page_search='all', competition_id=''):
    competition_menu = dict()

    page_search = page_search
    code_id = competition_id

    pages = ['standings', 'matches', 'teams', 'scorers', 'pl', 'all']

    for i in pages:
        if i == 'pl':
            code_id = ''
            adress = f'{code_id}/{i}'
        elif i == 'all':
            adress = ''
        else:
            adress = f'{code_id}/{i}'
        competition_menu[i] = adress

    page_adress = f'/competitions/{competition_menu[page_search]}'

    return page_adress
