
import re

def make_height_integer(players = []):
    for player in players:
        player['height'] = int(re.search(r'\d+', player['height']).group())
    return players

def make_experience_boolean(players = []):
    for player in players:
        player['experience'] = player['experience'] == 'YES'
    return players

def make_guardians_list(players = []):
    for player in players:
        player['guardians'] = player['guardians'].split(' and ')
    return players

def distribute_list_items_equally(items=[], groups=[]):
    num_of_teams = len(groups)
    if len(items) % num_of_teams != 0:
        raise ValueError('Number of items is not divisible by number of groups')
    items_grouped_arrays = [{} for _ in range(num_of_teams)]
    number_items_in_each_group = len(items) // num_of_teams
    stop = number_items_in_each_group
    start = 0
    for  val in groups:
        items_grouped_arrays[0][val] = items[start:stop]
        start = stop
        stop += number_items_in_each_group
    return items_grouped_arrays

def sort_for_experience(players=[]):
    # Separate experienced and inexperienced players
    experienced = [player for player in players if player['experience']]
    inexperienced = [player for player in players if not player['experience']]

    result = []

    # Alternate between experienced and inexperienced players
    while experienced or inexperienced:
        if experienced:
            result.append(experienced.pop(0))
        if inexperienced:
            result.append(inexperienced.pop(0))

    return result


