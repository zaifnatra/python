def get_option():
    try:
        option = int(input("Choose an option: "))
        return option
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_option()

### not sure if thsi is right place for this function, but it is used in main.py
### check out how to work for main after
def get_filename():
    filename = input("Enter the filename: ").strip()
    if not filename:
        print("Filename cannot be empty. Please try again.")
        return get_filename()
    return filename

### test
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BasketballPlayer, FootballPlayer

def load_file(filename):
    athletes = []

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or ":" not in line:
                    continue

                athlete_type, data = line.split(":", 1)
                athlete_type = athlete_type.strip()
                data = data.strip()

                if athlete_type == "HockeyPlayer":
                    athlete = HockeyPlayer.parse(data)
                elif athlete_type == "Swimmer":
                    athlete = Swimmer.parse(data)
                elif athlete_type == "BasketballPlayer":
                    athlete = BasketballPlayer.parse(data)
                elif athlete_type == "FootballPlayer":
                    athlete = FootballPlayer.parse(data)
                else:
                    continue 

                athletes.append(athlete)

    except Exception as e:
        print("Something went wrong while reading the file.")
        print("Error:", e)  # <--- temporary for debugging


    return athletes
