class Team:

    def __init__(self, team: dict):
        self.__area = team['area']
        self.__code_id = team['id']
        self.__name = team['name']

        self.details = {"shortName": team['shortName'],
                        "tla": team['tla'],
                        "crest": team['crest'],
                        "address": team['address'],
                        "website": team['website'],
                        "founded": team['founded'],
                        "clubColors": team['clubColors'],
                        "venue": team['venue'],
                        "runningCompetitions": team['runningCompetitions'],
                        "lestUpdated": team['lastUpdated']}

        self.running_competitions = team['runningCompetitions']

        self.rh = {'coach': team['coach'],
                   'squad': team['squad'],
                   'staff': team['staff']}

    @property
    def area(self):
        return self.__area

    @property
    def code_id(self):
        return self.__code_id

    @property
    def name(self):
        return self.__name
