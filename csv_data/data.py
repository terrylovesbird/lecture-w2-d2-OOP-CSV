from nfl_team import NflTeam
import csv

team_data = NflTeam.load_all_teams()
team_data.append(NflTeam(4, "Giants", wins=6, losses=10))
team_data.append(NflTeam(5, "Lion", wins=8, losses=8))

NflTeam.write_teams_to_file(team_data)

print("done!")
