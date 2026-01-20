
from insurance_calculator import InsuranceCalculator
from object_formatter import ObjectFormatter
from src.solid_principles.car import Car
from src.solid_principles.truck import Truck


def main():
    car=Car("Toyota","Camry",2018)
    truck=Truck("Ford","F-150",2015)
    insurance_calculator = InsuranceCalculator()
    formatter = ObjectFormatter()
    print(f"Car Insurance Cost: ${insurance_calculator.calculate_vehicle_insurance(car)}")
    print(f"Truck insurance cost: ${insurance_calculator.calculate_vehicle_insurance(truck)}")
    print(f"Vehicle Details in JSON:v {formatter.vehicle_to_json(car)}")


if __name__ == "__main__":
    main()

