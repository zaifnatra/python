from athlete import Athlete

class Swimmer(Athlete):
    total_swimmers = 0

    def __init__(self, name, age, stroke_style, country=None, salary=None, personal_best_time=None):
        super().__init__(name, age, country, salary)
        self.stroke_style = stroke_style
        self.personal_best_time = float(personal_best_time) if personal_best_time else None

        Swimmer.total_swimmers += 1
        print(f"Swimmer '{self.name}', {self.age} created; total # of swimmers {Swimmer.total_swimmers}.")

    def printStats(self):
        super().printStats()
        pb_time = f"{self.personal_best_time:.2f}s" if self.personal_best_time is not None else "N/A"
        print(f"Stroke Style: {self.stroke_style}, Personal Best Time: {pb_time}")

    @staticmethod
    def parse(text):
        parts = [p.strip() for p in text.split(",")]
        while len(parts) < 6:
            parts.append(None)
    ### if few than 6 values, fill with nothing
        name = parts[0]
        age = parts[1]
        stroke_style = parts[2]
        country = parts[3]
        salary = parts[4]
        personal_best_time = parts[5]

        return Swimmer(name, age, stroke_style, country, salary, personal_best_time)
