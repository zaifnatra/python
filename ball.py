from athlete import Athlete

class BallPlayer(Athlete):
    total_ball_players = 0

    def __init__(self, name, age, country, salary, team_name=None, jersey_number=None, endorsement=None):
        super().__init__(name, age, country, salary)
        self.team_name = team_name
        self.jersey_number = int(jersey_number) if jersey_number else None
        self.endorsement = endorsement

        BallPlayer.total_ball_players += 1
        print(f"Ball Player '{self.name}', {self.age} created; total # of ball players {BallPlayer.total_ball_players}.")

    def printEndorsement(self):
        print(f"Endorsement: {self.endorsement if self.endorsement else 'None'}")
#basketball player
class BasketballPlayer(BallPlayer):
    total_basketball_players = 0

    def __init__(self, name, age, country, salary, team_name, jersey_number,
                 endorsement=None, three_point_pct=None, rebounds=None):
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)
        self.three_point_pct = float(three_point_pct) if three_point_pct else None
        self.rebounds = int(rebounds) if rebounds else None

        BasketballPlayer.total_basketball_players += 1
        print(f"Basketball Player '{self.name}', {self.age} created; total # of basketball players {BasketballPlayer.total_basketball_players}.")

    def printStats(self):
        super().printStats()
        print(f"Team: {self.team_name}, Jersey #: {self.jersey_number}, "
              f"3 Point %: {self.three_point_pct if self.three_point_pct is not None else 'N/A'}, "
              f"Rebounds: {self.rebounds if self.rebounds is not None else 'N/A'}")

    @staticmethod
    def parse(text):
        parts = [p.strip() for p in text.split(",")]
        while len(parts) < 9:
            parts.append(None)

        return BasketballPlayer(parts[0], parts[1], parts[4], parts[5],  
                                parts[2], parts[3],                       
                                parts[6], parts[7], parts[8])            

#football player
class FootballPlayer(BallPlayer):
    total_football_players = 0

    def __init__(self, name, age, country, salary, team_name, jersey_number,
                 endorsement=None, touchdowns=None, passing_yards=None):
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)
        self.touchdowns = int(touchdowns) if touchdowns else None
        self.passing_yards = int(passing_yards) if passing_yards else None

        FootballPlayer.total_football_players += 1
        print(f"Football Player '{self.name}', {self.age} created; total # of football players {FootballPlayer.total_football_players}.")

    def printStats(self):
        super().printStats()
        print(f"Team: {self.team_name}, Jersey #: {self.jersey_number}, "
              f"Touchdowns: {self.touchdowns if self.touchdowns is not None else 'N/A'}, "
              f"Passing Yards: {self.passing_yards if self.passing_yards is not None else 'N/A'}")

    @staticmethod
    def parse(text):
        parts = [p.strip() for p in text.split(",")]
        while len(parts) < 9:
            parts.append(None)

        return FootballPlayer(parts[0], parts[1], parts[4], parts[5],  
                              parts[2], parts[3],                      
                              parts[6], parts[7], parts[8])           
