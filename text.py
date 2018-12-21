import json
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams

if __name__ == '__main__':
    user_input = 'who is the coach of the Celtics'
    unicode_input = u'{}'.format(user_input)

    with open('data/teams.json') as f:
        data = json.load(f)

        for entry in data:
            team_abv = json.dumps(entry['abbreviation'])

            if entry['teamName'] in unicode_input:
                team_id = entry['teamId']
                team_name = etrny['']
            elif entry['teamName'] in unicode_input:
                team_id = entry['teamId']
            elif entry['location'] in unicode_input:
                team_id = entry['teamId']
            elif entry['simpleName'] in unicode_input:
                team_id = entry['teamId']


    if team_id != '':
        team_roster = commonteamroster.CommonTeamRoster(team_id=team_id).coaches.get_dict()

        team_name = teams.find_team_name_by_id(team_id)
        print(team_name['nickname'])
    else:
        print('Was not able to find that team')
