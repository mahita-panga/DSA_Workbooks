"""
Factory Pattern  -> Creational pattern which provides an interface for creating
objects in superclass but allows subclasses to alter the type of objects created.

Example: Think of a factory which is producing different varieties of product and
this can expand in future to a scale where we might need to add more products to our application
So, instead of tightly coupling to one particular product type, we create a interface which has the
methods to produce items. How these items are produced will be implemented in the subclasses.

-> Used in Payment Instances where different payment gateway instances need to be created

"""
#Lets say we are producing cars and trucks now. We can produce flights later as well.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        vehicles = {
            "car": Car(),
            "truck": Truck()
        }
        return vehicles.get(vehicle_type.lower(),None)


class Truck(Vehicle):
    def create_vehicle(self):
        return 'Truck Created 🚛'

class Car(Vehicle):
    def create_vehicle(self):
        return 'Car created 🚗'



factory = VehicleFactory()
car = factory.get_vehicle('car') #Returns car instance
print(car.create_vehicle())

truck = factory.get_vehicle('Truck')
print(truck.create_vehicle())

