from access.capture_source import create_file_request


def all_areas_dict_with_not_allowed():
    all_areas = dict()

    area_page = 'areas/'
    areas_from_source = create_file_request(area_page)

    all_areas['all'] = ''
    for i in areas_from_source['areas']:
        all_areas[i['name']] = i

    return all_areas


def print_all_area_id_with_not_allowed(all_areas: dict):
    print(all_areas)
    for area in all_areas:
        print(f'{area}: {all_areas[area]}')


teste = all_areas_dict_with_not_allowed()
print_all_area_id_with_not_allowed(teste)
