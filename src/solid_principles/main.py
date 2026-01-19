from pygments import formatter

from insurance_calculator import InsuranceCalculator
from object_formatter import ObjectFormatter
from src.solid_principles.vehicle import Vehicle


def main():
    vehicle = Vehicle("Toyota", "Camry", 2018)
    insurance_calculator = InsuranceCalculator()
    formatter = ObjectFormatter()
    print("Car Insurance Cost: ${insurance_calculator.calculate_car_insurance{vehicle}}")
    print(f"Vehicle Details in JSON: {formatter.vehicle_to_json(vehicle)}")

if __name__ == "__main__":
    main()

