from src.solid_principles.vehicle import Vehicle


class Car(Vehicle):
    def calculate_insurance(self):
        age = 2024 - self.year
        return 1000 if age > 5 else 500

    def refuel(self):
        print("Refueling the car with petrol....")
