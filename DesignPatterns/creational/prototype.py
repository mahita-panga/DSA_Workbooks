"""
Prototype Pattern - used for creating copy of objects without making code dependent on their classes

Used when you want to create copy of objects for an exising class and we dont know the behaviour of the class
we don't know what private methods or fields are there in the class.
So to make an extra copy of the object, there is a dependency on the class, Sometimes we only know the interface
that object follows and not its concrete class.
This is where prototype is used

-> The pattern declares a common interface for all objects that support cloning <- THIS interface is just a clone() method
-> Object that supports cloning - Prototype

In real life: prototypes are used for performing various tests before starting mass production of a product.

Example: Prototypes to clone Car class objects
"""

import copy

class Prototype: #Prototype Registry
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object."""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object."""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes."""
        # creating a new completely separate copy of the name object in memory
        obj = copy.deepcopy(self._objects.get(name))
        # Updating the attributes of obj with the keys and values in attr.
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self,name,color,options):
        self.name = name
        self.color = color
        self.options = options

    def __str__(self):
        return f'{self.name} | {self.color} | {self.options}'

brezza_car = Car('Brezza','red','Ex')
creta_car = Car('Creta','black','New')

prototype = Prototype()
prototype.register_object('Brezza', brezza_car)
prototype.register_object('Creta', creta_car)

car1 = prototype.clone('Brezza')
car2 = prototype.clone('Creta')

print(car1)
print(car2)