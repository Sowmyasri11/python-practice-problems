from insurance_calculator import InsuranceCalculator
from object_formatter import ObjectFormatter
from src.solid_principles.break_inspection_tool import BreakInspectionTool
from src.solid_principles.car import Car
from src.solid_principles.electric_car import ElectricCar
from src.solid_principles.maintenance_service import MaintenanceService
from src.solid_principles.truck import Truck


def main():
    car = Car("Toyota", "Camry", 2018)
    truck = Truck("Ford", "F-150", 1980)
    electric_car=ElectricCar("Tesla", "Model 3",2021)

    car.refuel()
    truck.refuel()
    electric_car.recharge()
    car.refuel()


    insurance_calculator = InsuranceCalculator()
    formatter = ObjectFormatter()

    print(f"Car Insurance Cost: ${insurance_calculator.calculate_vehicle_insurance(car) + 100}")
    print(f"Truck insurance cost: ${insurance_calculator.calculate_vehicle_insurance(truck) + 100}")
    print(f"Car Details in JSON: {formatter.vehicle_to_json(car)}")
    print(f"Truck Details in JSON: {formatter.vehicle_to_json(truck)}")

    service = MaintenanceService(BreakInspectionTool())
    service.service_vehicle(car)
    service.service_vehicle(truck)

if __name__ == "__main__":
    main()
