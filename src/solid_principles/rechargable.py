from abc import ABC, abstractmethod

class Rechargable(ABC):

    @abstractmethod
    def recharge(self):
        pass