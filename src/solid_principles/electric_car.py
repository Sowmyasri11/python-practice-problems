from src.solid_principles.car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_insurance(self):
        age = 2024 - self.year

        return 2000 if age > 5 else 1000

    def refuel(self):
        raise Exception("Electric Car cannot be refueled. ")
