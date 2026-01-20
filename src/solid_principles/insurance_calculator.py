from src.solid_principles.vehicle import Vehicle


class InsuranceCalculator:
    def calculate_vehicle_insurance(self, vehicle: Vehicle):
        return vehicle.calculate_insurance()
