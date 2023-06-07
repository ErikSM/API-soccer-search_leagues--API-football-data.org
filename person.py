
def white_person_page_adress(page_search, person_id):
    person_menu = dict()
    person_menu['particular'] = f'{person_id}'
    person_menu['matches'] = f'{person_id}/matches'

    adress_page = f'persons/{person_menu[page_search]}'

    return adress_page
