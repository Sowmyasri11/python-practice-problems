from src.solid_principles.maintenance_tool import MaintenanceTool
from src.solid_principles.vehicle import Vehicle


class BreakInspectionTool(MaintenanceTool):
    def perform_maintenance(self, vehicle:Vehicle):
        print(f"Performing brake inspection on {vehicle.make} {vehicle.model}".format(vehicle=vehicle))
