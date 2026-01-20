from src.solid_principles.vehicle import Vehicle


class Truck(Vehicle):
    def calculate_insurance(self):
        age=2024-self.year
        return 1500 if age > 8 else 700