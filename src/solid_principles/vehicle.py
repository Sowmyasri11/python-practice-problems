import json


class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_insurance_cost(self):
        age = 2024 - self.year
        if age > 5:
            return 1000
        return 500

    def to_json(self):
        return json.dumps({
            "VehicleMake": self.make,
            "VehicleModel": self.model,
            "VehicleYear": self.year
        })

def main():
    vehicle = Vehicle("Honda", "Mercedes", "2022")
    print(f"Insurance cost: ${vehicle.calculate_insurance_cost()}")
    print(f"Vehicle details in JSON: {vehicle.to_json()}")


if __name__ == "__main__":
    main()