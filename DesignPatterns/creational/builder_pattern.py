"""
This is a creational pattern which helps us to construct complex objects step by step
This is useful when you are creating objects with many possible configuration setups

-> https://refactoring.guru/design-patterns/builder

Lets say we are building a house. A house can have garden, garage, swimming pool, statues, foyer etc.
We can build in whatever configuration user wants.
If we create a class like:
class House:
    def __init__(self, hasGarage, hasPool, hasStatues...):

constructor is going to be messy and confusing.
So, builder pattern helps where we do:
house.createpool()
house.creategarage()
.. as needed

4 roles:
- Product: End result
- Builder: interface which defines steps to build
- Concrete Builder: concrete class to construct and aggregate as needed
- Director: Optional class : Manager the sequence of steps. Works with builder to create the object

Example:
    We are building a car with various factors

"""
from abc import ABC,abstractmethod
#Product
class Car:
    def __init__(self):
        self.engine = None
        self.model = None

#Builder
class Builder(ABC):
    @abstractmethod
    def make_model(self):
        pass
    @abstractmethod
    def make_engine(self):
        pass

#Concrete Builder
class BmWBuilder(Builder):
    def __init__(self):
        self.car = Car() #we are making a car

    def make_model(self):
        self.car.model = "BMW X5"
    def make_engine(self):
        self.car.engine = "V8"

    def get_car(self):
        return self.car

class AudiBuilder(Builder):
    def __init__(self):
        self.car = Car() #we are making a car

    def make_model(self):
        self.car.model = "Audi Q7"
    def make_engine(self):
        self.car.engine = "V6"

    def get_car(self):
        return self.car

#Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_car(self):
        self.builder.make_model()
        self.builder.make_engine()
        return self.builder.get_car()

audi_builder = AudiBuilder()
director = Director(audi_builder)
car = director.build_car()
print(f"Build {car.model} with {car.engine}")

bmw_builder = BmWBuilder()
director.builder = bmw_builder
car = director.build_car()
print(f"Build {car.model} with {car.engine}")
