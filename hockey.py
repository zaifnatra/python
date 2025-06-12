from athlete import Athlete
from enum import Enum

class HockeyPosition(Enum):
    FORWARD = "Forward"
    DEFENSEMAN = "Defenseman"
    GOALIE = "Goalie"

class HockeyPlayer(Athlete):
    total_hockey_players = 0

    def __init__(self, name, age, country=None, salary=None, position=None,
                 goals_scored=None, stick_brand=None, skates_size=None):
        super().__init__(name, age, country, salary)
        self.position = HockeyPosition(position) if position else None
        self.goals_scored = int(goals_scored) if goals_scored else 0
        self.stick_brand = str(stick_brand) if stick_brand else "N/A"
        self.skates_size = int(skates_size) if skates_size else 0

        HockeyPlayer.total_hockey_players += 1
        print(f"Hockey Player '{self.name}', {self.age} created; total # of hockey players {HockeyPlayer.total_hockey_players}.")

    def printStats(self):
        super().printStats()
        print(f"Position: {self.position.value if self.position else 'Unknown'}, "
              f"Goals Scored: {self.goals_scored}, "
              f"Stick Brand: {self.stick_brand}, "
              f"Skates Size: {self.skates_size}")

    @staticmethod
    def parse(text):
        parts = [p.strip() for p in text.split(",")]
        while len(parts) < 8:
            parts.append(None)
 ### if few than 8 values, fill with nothing
        name = parts[0]
        age = parts[1]
        country = parts[2]
        salary = parts[3]
        position = parts[4]
        goals_scored = parts[5]
        stick_brand = parts[6]
        skates_size = parts[7]

        return HockeyPlayer(name, age, country, salary, position, goals_scored, stick_brand, skates_size)
