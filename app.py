import constants as c
import functions as f


players = c.PLAYERS
teams = c.TEAMS

cleaned_players = f.make_height_integer(players)
cleaned_players = f.make_experience_boolean(cleaned_players)
cleaned_players = f.make_guardians_list(cleaned_players)
cleaned_players = f.sort_for_experience(cleaned_players)

teams_equally_distributed = f.distribute_list_items_equally(cleaned_players, teams)

def start():
    print('BASKETBALL TEAM STATS TOOL\n')
    print('---- MENU ----\n')
    print('Here are your choices:\n')
    for i, val in enumerate(teams):
        print(f'{i+1}) {val}')

    selection = input('\nEnter an option: ')

    if int(selection) > len(teams):
        print('Invalid selection. Please try again.')
        start()

    print(f'\nTeam: {teams[int(selection)-1]} Stats\n')

    selection = int(selection) - 1
    selected_team_name = teams[selection]
    selected_team = teams_equally_distributed[0][selected_team_name]

    print(f'Total players: {len(selected_team)}\n')
    print(f'Total experienced: {len([player for player in selected_team if player["experience"]])}')
    print(f'Total inexperienced: {len([player for player in selected_team if not player["experience"]])}\n')
    print(f'Average height: {sum([player["height"] for player in selected_team]) / len(selected_team)}\n')

    print('Players on Team:')
    players = [player['name'] for player in selected_team]
    print(', '.join(players))

    print('\nGuardians: ')
    guardians = []
    for player in selected_team:
        if type(player['guardians']) == list:
            for guardian in player['guardians']:
                guardians.append(guardian)
        else:
            guardians.append(player['guardians'])
    print(', '.join(guardians))

    user_input = input("Press Enter to continue...\n")
    if user_input == "":
        start()



if __name__ == '__main__':
    start()