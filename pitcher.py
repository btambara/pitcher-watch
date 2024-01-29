import statsapi

player = statsapi.lookup_player("Kershaw", season=2023)[0]

if player:
    team_id = player["currentTeam"]["id"]
    team_schedule = statsapi.schedule(team=team_id, start_date="2023-01-01", end_date="2023-12-31")
    pitch_types = {}

    for game in team_schedule:
        game_data = statsapi.get("game_playByPlay", {"gamePk": game["game_id"]})
        for play in game_data["allPlays"]:
            current_pitcher = play["matchup"]["pitcher"]["id"]
            for event in play["playEvents"]:
                if "eventType" in event["details"] and event["details"]["eventType"] == "pitching_substitution":
                    current_pitcher = event["player"]["id"]
                elif current_pitcher ==  player["id"] and event["isPitch"] and "type" in event["details"]:
                    pitch_type = event["details"]["type"]["description"]
                    
                    if pitch_type not in pitch_types:
                        pitch_types[pitch_type] = 1
                    else:
                        pitch_types[pitch_type] = pitch_types[pitch_type] + 1

    print("Pitcher: " + player["fullName"])
    print(pitch_types)
else:
    print("No pitchers found.")