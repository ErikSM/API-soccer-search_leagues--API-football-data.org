from access.capture_source import write_sub_resource_page_address, create_file_request
from resources.match import match_resources_tuple


def open_resource_info(resource_tuple: tuple, page_search: str = None, code_id: str = None):
    if page_search is None and code_id is None:
        address = write_sub_resource_page_address(resource_tuple)
    else:
        address = write_sub_resource_page_address(resource_tuple, page_search, code_id)

    dict = create_file_request(address)
    print(dict)

    return dict


open_resource_info(match_resources_tuple)
