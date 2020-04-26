from os import listdir
import json
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
                formatted_name = format_player_key(player[0])
                player_map[formatted_name] = Competitor(formatted_name,player[1])

    return player_map

def report_set(player_map, player_1_results, player_1_key, player_2_key):
    if player_1_results["standing"]["placement"] is 1:
        player_map[player_1_key].increment_w_l('W')
        player_map[player_2_key].increment_w_l('L')
    else:
        player_map[player_1_key].increment_w_l('L')
        player_map[player_2_key].increment_w_l('W')

def format_player_key(full_name):
    pos = full_name.find('|') + 1
    name_no_sponsor = full_name[pos:].strip()
    while '|' in name_no_sponsor:
        pos = name_no_sponsor.find('|') + 1
        name_no_sponsor = name_no_sponsor[pos:].strip()
    return name_no_sponsor

# Build map that we'll load all the data into
player_map = parse_gender_map_into_competitor_objects()

# Build a list of the set results files
sets_dir =  "/Users/noah.denier/repo/psychology-research/data/data/sets/"
events_dirs = listdir(sets_dir)
listOfSetResultFiles = []
for event in events_dirs:
    event_dir = sets_dir + event + '/'
    event_files = listdir(event_dir)
    for f in event_files:
        full_path = event_dir + f
        listOfSetResultFiles.append(full_path)


for f in listOfSetResultFiles:
    with open(f) as set_results_file:
        set_results_json = json.load(set_results_file)
        for set in set_results_json["data"]["event"]["sets"]["nodes"]:
            player_1_results = set["slots"][0]
            player_2_results = set["slots"][1]
            player_1_key = format_player_key(player_1_results["entrant"]["name"])
            player_2_key = format_player_key(player_2_results["entrant"]["name"])
            if player_1_key not in player_map:
                player_map[player_1_key] = Competitor(player_1_key,'U')
            if player_2_key not in player_map:
                player_map[player_2_key] = Competitor(player_2_key,'U')
            report_set(player_map, player_1_results, player_1_key, player_2_key)

results_list_form = []
results_list_form.append(['Gamertag','Gender','Wins','Losses'])
for player in player_map.items():
    player_list_form = []
    player_list_form.append(player[1].gamertag)
    player_list_form.append(player[1].gender)
    player_list_form.append(player[1].wins)
    player_list_form.append(player[1].losses)
    results_list_form.append(player_list_form)

with open('/Users/noah.denier/repo/psychology-research/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results_list_form)
