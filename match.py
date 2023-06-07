from main import create_file_request


def create_all_matches_dict():
    all_matches = dict()

    page_name = 'matches/'
    dict_from_source = create_file_request(page_name)

    for item in dict_from_source['matches']:
        all_matches[item['id']] = item

    return all_matches


def print_all_competitions_allowed(all_matches: dict):
    for i in all_matches:
        print(i)
        print(all_matches[i])


def write_match_page_adress(page_search, match_id=''):
    match_menu = dict()

    match_menu['all'] = ''
    match_menu['particular'] = f'{match_id}'
    match_menu['head2head'] = f'{match_id}/head2head'

    adress = f'matches/{match_menu[page_search]}'

    return adress




