from src.solid_principles.fuelable import Fuelable
from src.solid_principles.vehicle import Vehicle


class Truck(Vehicle,Fuelable):
    def calculate_insurance(self):
        age = 2024 - self.year
        return 1500 if age > 8 else 700

    def refuel(self):
        print("Refueling the truck with diesel....")

