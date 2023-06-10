from access.capture_source import create_file_request

match__menu_list = ['all', 'particular', 'head2head']
match_resources_tuple = ('matches', match__menu_list)


def all_matches_with_not_allowed_dict():
    all_matches = dict()

    page_name = 'matches/'
    dict_from_source = create_file_request(page_name)

    print(dict_from_source)
    for i in dict_from_source:
        if i == 'matches':
            continue
        else:
            print(i)

    for item in dict_from_source['matches']:
        all_matches[item['id']] = item

    return all_matches


def print_all_matches_with_not_allowed(all_matches: dict):
    for i in all_matches:
        print(i)
        print(all_matches[i])


'''teste = all_matches_with_not_allowed_dict()
print_all_matches_with_not_allowed(teste)'''
