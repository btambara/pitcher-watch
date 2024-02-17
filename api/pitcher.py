import statsapi
from datetime import datetime

to_year = datetime.now().year
player = statsapi.lookup_player("Kershaw", season=to_year)[0]
from_year = datetime.strptime(player["mlbDebutDate"], "%Y-%m-%d").year
for person in statsapi.get("sports_players", {"sportId": 1, "season": 2024})["people"]:
    print(person)
    print(person["currentTeam"]["id"])
# print(statsapi.get("sports_players", {"sportId": 1, "season": 2024})["people"][0])
# print(statsapi.player_stat_data(player["id"], group="pitching", type="career"))
# print("[")
# for stat in statsapi.meta("baseballStats"):
#     pitch_stats = {}
#     if "statGroups" in stat:
#         for group in stat["statGroups"]:
#             if group["displayName"] == "pitching":
#                 if "name" in stat:
#                     pitch_stats["name"] = stat["name"]
#                 else:
#                     pitch_stats["name"] = ""
#                 if "lookupParam" in stat:
#                     pitch_stats["lookupParam"] = stat["lookupParam"]
#                 else:
#                     pitch_stats["lookupParam"] = ""
#                 if "label" in stat:
#                     pitch_stats["label"] = stat["label"]
#                 else:
#                     pitch_stats["label"] = ""
                
#                 print(str(pitch_stats) + ",")
# print("]")

if not player:
    team_id = player["currentTeam"]["id"]
    json_string = {}
    pitch_list = []

    for year in range(from_year, to_year, 1):
        print(year)
        pitches = {}
        pitches["year"] = year
        team_schedule = statsapi.schedule(team=team_id, start_date=str(year) + "-01-01", end_date=str(year) + "-12-31")
        pitch_types = {}
        
        for game in team_schedule:
            if game["game_type"] == "R":
                game_data = statsapi.get("game_playByPlay", {"gamePk": game["game_id"]})
                for play in game_data["allPlays"]:
                    current_pitcher = play["matchup"]["pitcher"]["id"]
                    for event in play["playEvents"]:
                        if "eventType" in event["details"] and event["details"]["eventType"] == "pitching_substitution":
                            current_pitcher = event["player"]["id"]
                        elif current_pitcher ==  player["id"] and event["isPitch"] and "type" in event["details"]:
                            pitch_type = event["details"]["type"]["code"]
                            
                            if pitch_type not in pitch_types:
                                pitch_types[pitch_type] = 1
                            else:
                                pitch_types[pitch_type] = pitch_types[pitch_type] + 1

        print("Pitcher: " + player["fullName"])
        print("Year: " + str(year))
        print("Regular Season")
        print("Pitch Types:")
        print(pitch_types)
        print()

        totalPitches = 0

        for pitch in pitch_types:
            pitch_list.append({
                "code": pitch,
                "amount": pitch_types[pitch]
            })
            totalPitches += int(pitch_types[pitch])
        
        pitches["pitches"] = pitch_list
        print("Total pitches: " + str(totalPitches))
    
    json_string["fullName"] = player["fullName"]
    json_string["primaryNumber"] = player["primaryNumber"]
    json_string["primaryPosition"] = player["primaryPosition"]["abbreviation"]
    json_string["pitches"] = pitches

    print("---JSON")    
    print(json_string)
else:
    print("No pitchers found.")