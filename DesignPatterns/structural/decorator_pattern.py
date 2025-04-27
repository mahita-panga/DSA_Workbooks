"""
Decorator Pattern -> used when we want to add new behaviors or responsibilities to objects dynamically, without modifying their code.

The decorator class implements the same interface as the object it decorates.

You can "wrap" an object inside multiple decorators to add combined behavior.

-> https://refactoring.guru/design-patterns/decorator

Analogy:
Think of a plain coffee ☕.
You can add milk 🥛, then sugar 🍬, then whipped cream 🍦 as you wish.
Each addition (decorator) enhances the coffee but does not modify the original coffee class.
You can "stack" decorators flexibly to create different types of coffee.

Scenario:
Used when you need to dynamically add responsibilities to objects, like adding features (e.g., toppings on food orders, additional visual effects on UI elements) without making a mess inside the original classes.


"""

from abc import ABC, abstractmethod


#INTERFACE
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


#BASE COMPONENT
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple Coffee"


#BASE DECORATOR
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


#DECORATOR-1
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2

    def description(self):
        return super().description() + ", with Milk 🥛"


#DECORATOR-2
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1

    def description(self):
        return super().description() + ", with Sugar 🍬"


#DECORATOR-3
class WhipCreamDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 3

    def description(self):
        return super().description() + ", with Whip Cream 🍦"


#USAGE/CLIENT
coffee = SimpleCoffee()
print(f"{coffee.description()} : ${coffee.cost()}")

# Add Milk
coffee = MilkDecorator(coffee)
print(f"{coffee.description()} : ${coffee.cost()}")

# Add Sugar
coffee = SugarDecorator(coffee)
print(f"{coffee.description()} : ${coffee.cost()}")

# Add Whip Cream
coffee = WhipCreamDecorator(coffee)
print(f"{coffee.description()} : ${coffee.cost()}")
