import csv
from competitor import Competitor

def parse_gender_map_into_competitor_objects():
    player_map = {}
    with open('/Users/noah.denier/repo/psychology-research/data/gender_map.csv') as gender_csv_file:
        gender_map = csv.reader(gender_csv_file, delimiter=',')
        line_count = 0
        for player in gender_map:
            if line_count == 0:
                print(f'Column names are {", ".join(player)}')
                line_count += 1
            else:
                player_map[player[0]] = Competitor(player[0],player[1])

    return player_map

player_map = parse_gender_map_into_competitor_objects()

player_map['MkLeo'].report_set('Frostbite','W')
print(player_map['MkLeo'].set_history)
print(player_map['MkLeo'].gender)
print(player_map['MkLeo'].gamertag)
