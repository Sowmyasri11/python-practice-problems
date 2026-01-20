from src.solid_principles.car import Car
from src.solid_principles.truck import Truck
from src.solid_principles.vehicle import Vehicle


class InsuranceCalculator:
    def calculate_vehicle_insurance(self, vehicle: Vehicle):

        age = 2024 - vehicle.year
        if isinstance(vehicle, Car):
            return 1000 if age > 5 else 500
        elif isinstance(vehicle, Truck):
            return 1500 if age > 8 else 700


        if age > 5:
            return 1000
        return 500
