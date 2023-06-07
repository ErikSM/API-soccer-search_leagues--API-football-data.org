from main import create_file_request


def create_allowed_teams_dict():
    all_teams = dict()

    page_name = 'teams/'
    dict_from_source = create_file_request(page_name, False)

    for item in dict_from_source['teams']:
        all_teams[item['name']] = item

    return all_teams


def white_teams_page_adress(page_search='all', team_id=''):
    teams_menu = dict()

    teams_menu['all'] = ''
    teams_menu['particular'] = f'{team_id}'
    teams_menu['matches'] = f'{team_id}/matches/'

    adress_team = f'teams/{teams_menu[page_search]}'

    return adress_team
