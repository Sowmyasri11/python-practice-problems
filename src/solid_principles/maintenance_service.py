from src.solid_principles.break_inspection_tool import BreakInspectionTool
from src.solid_principles.maintenance_tool import MaintenanceTool
from src.solid_principles.vehicle import Vehicle


class MaintenanceService:
    def __init__(self, tool: MaintenanceTool):
        self.tool = tool

    def service_vehicle(self, vehicle: Vehicle):
        self.tool.perform_maintenance(vehicle)
