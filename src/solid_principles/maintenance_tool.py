from abc import ABC, abstractmethod

from src.solid_principles.vehicle import Vehicle


class MaintenanceTool(ABC):

    @abstractmethod
    def perform_maintenance(self, vehicle: Vehicle):
        pass