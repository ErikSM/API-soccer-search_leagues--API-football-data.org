



area_pages_list = ['all', 'particular']
area_menu = ('areas', area_pages_list)


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
