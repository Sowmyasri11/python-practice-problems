from src.solid_principles.car import Car
from src.solid_principles.rechargable import Rechargable
from src.solid_principles.vehicle import Vehicle


class ElectricCar(Vehicle,Rechargable):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_insurance(self):
        age = 2024 - self.year

        return 2000 if age > 5 else 1000

    def recharge(self):
        print("Recharging Electric Car. ")
