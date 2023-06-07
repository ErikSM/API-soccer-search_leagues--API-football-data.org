from main import create_file_request


def create_all_areas_dict():
    all_areas = dict()

    area_page = 'areas/'
    areas_from_source = create_file_request(area_page)

    all_areas['all'] = ''
    for i in areas_from_source['areas']:
        all_areas[i['name']] = i

    return all_areas


def print_area_id(all_areas: dict):
    print(all_areas)
    for area in all_areas:
        print(f'{area}: {all_areas[area]}')

