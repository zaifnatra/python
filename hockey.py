from athlete import Athlete
from enum import Enum

class HockeyPosition(Enum):
    FORWARD = "Forward"
    DEFENSEMAN = "Defenseman"
    GOALIE = "Goalie"


class HockeyPlayer(Athlete):
    def __init__(self, name, age, country, salary, position, goals_scored, stick_brand, skates_size):
        super().__init__(name, age, country, salary)
        self.position = HockeyPosition(position) 
        self.goals_scored = int(goals_scored)
        self.stick_brand = str(stick_brand)
        self.skates_size = int(skates_size)

    def printStats(self):
        super().printStats()
        print(f"Position: {self.position.value}, Goals Scored: {self.goals_scored}, "
              f"Stick Brand: {self.stick_brand}, Skates Size: {self.skates_size}")

    def printEndorsement(self):
        print("Endorsement data for Hockey Athlete is not available.")