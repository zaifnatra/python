class Athlete:
    total_athletes = 0

    def __init__(self, name, age, country, salary):
        self.name = str(name)
        self.age = int(age)
        self.country = str(country)
        self.salary = float(salary)

        Athlete.total_athletes += 1
        print(f"Athlete '{self.name}', {self.age} created; total # of athletes {Athlete.total_athletes}.")

    def printStats(self):
        print(f"Athlete Name: {self.name}, Age: {self.age}, Country: {self.country}, Salary: ${self.salary:}")

    def printEndorsement(self):
        print("No endorsement data available for base Athlete.")
