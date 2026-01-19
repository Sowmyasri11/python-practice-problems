from src.solid_principles.vehicle import Vehicle


class InsuranceCalculator:
    def calculate_car_insurance(self,vehicle:Vehicle):
        age = 2024 - self.year
        if age > 5:
            return 1000
        return 500