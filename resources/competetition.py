from access.capture_source import create_file_request

competition_menu_list = ['all', 'particular', 'standings', 'matches', 'teams', 'scorers']
competition_resources_tuple = ('competitions', competition_menu_list)


def all_competitions_with_not_allowed_dict():
    all_competitions = dict()

    page_name = 'competitions/'
    dict_from_source = create_file_request(page_name)

    for item in dict_from_source['competitions']:
        all_competitions[item['name']] = item

    return all_competitions


def print_all_competitions_with_not_allowed(all_competitions: dict):
    for i in all_competitions:
        print(i)
        print(all_competitions[i])


'''teste = all_competitions_with_not_allowed_dict()
print_all_competitions_with_not_allowed(teste)'''
