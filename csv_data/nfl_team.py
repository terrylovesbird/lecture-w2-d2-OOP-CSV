import csv

class NflTeam:
    total_games = 16
    
    def load_all_teams(cls):
        # using csv module using dictionary reader
        nfl_teams = []
        with open("data/nfl.csv", "r") as nfl_file:
            dict_reader = csv.DictReader(nfl_file)
            for line in dict_reader:
                nfl_teams.append(cls(**line))
        return nfl_teams 
    
    @classmethod
    def write_teams_to_file(cls, add_teams_list):
        with open('data/nfl.csv', mode='w') as nfl_file:
            nfl_writer = csv.DictWriter(nfl_file, ["id", "team", "wins", "losses"])
            nfl_writer.writeheader()
            for team in add_teams_list:
                print(team.__dict__)
                nfl_writer.writerow(team.__dict__)
    
    def __init__(self, id, team, losses, wins):
        self.id = id
        self.team = team
        self.wins = wins
        self.losses = losses

    def __str__(self):
        return f"{self.id}: The {self.team} have {self.wins} wins for this season"

    def get_win_pct(self):
        return self.wins / self.total_games


