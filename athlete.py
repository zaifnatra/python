class Athlete:
    def __init__(self, name, age, country, salary):
        self.name = str(name)
        self.age = int(age)
        self.country = str(country)
        self.salary = float(salary)

    def printStats(self):
        print(f"Athlete Name: {self.name}, Age: {self.age}, Country: {self.country}, Salary: ${self.salary:.2f}")

    def printEndorsement(self):
        print("No endorsement data available for base Athlete.")
