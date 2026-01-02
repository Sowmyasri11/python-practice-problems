from abc import ABC, abstractmethod

class Dog(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog's Name : {self.name}")

class Labrador(Dog):

    def sound(self):
        print("Labrador woof!")

class Beagle(Dog):

    def sound(self):
        print("Beagle Bark!")

dogs=[Labrador("Buddy"),Beagle("Charlie")]
for dog in dogs:
    dog.display_name()
    dog.sound()