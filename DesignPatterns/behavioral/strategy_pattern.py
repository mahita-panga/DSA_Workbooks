"""
Strategy Pattern -> used when a class does something specific in a lot of different ways and
extract all these algorithms into separate classes called "STRATEGIES"
Original Class if called CONTEXT.
- This has a field for storing references for the strategies.
- Context class delegates the work to a linked strategy object.

-> https://refactoring.guru/design-patterns/strategy

Analogy:
   Lets say we have to travel to Airport. We can reach via bus/train/car/cycle.
   Option to choose the mode of travel(Strategy) is dependent on certain factors like time/money etc.
   A interface in context is responsible for routing to use the required strategy based on factors.
   A new strategy class comes up, we don't have to edit the existing strategies or context class

Below code is for this example:
Think of a travel application where the user can choose different modes of transportation
(like car, train, flight) to reach the destination.
The choice of transportation can be changed dynamically based on user preference.

-> Used in scenarios where we need to switch between different algorithms or strategies on the fly.
"""

from abc import ABC, abstractmethod

#INTERFACE
class TravelStrategy(ABC):
    @abstractmethod
    def travel(self,start,end):
        pass

#STRATEGY-1
class CarStrategy(TravelStrategy):
    def travel(self,start,end):
        return f"Driving from {start} to {end} via a car 🚗"

#STRATEGY-2
class TrainStrategy(TravelStrategy):
    def travel(self,start,end):
        return f"Driving from {start} to {end} via train 🚂"

#STRATEGY-3
class BusStrategy(TravelStrategy):
    def travel(self,start,end):
        return f"Driving from {start} to {end} via bus 🚌"

#STRATEGY-4
class FlightStrategy(TravelStrategy):
    def travel(self,start,end):
        return f"Flying from {start} to {end} via flight ✈️"

#CONTEXT
class TravelContext:
    def __init__(self, strategy: TravelStrategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: TravelStrategy):
        self._strategy = strategy

    def arrange_travel(self,start,end):
        return self._strategy.travel(start,end)


#USAGE/CLIENT
context = TravelContext(CarStrategy())
print(context.arrange_travel("Bangalore","Hyderabad"))

#strategies can be changed on fly
context.strategy = TrainStrategy()
print("Now Arranging travel via a train")
print(context.arrange_travel("Hyderabad","Vijawayada"))

context.strategy = FlightStrategy()
print(context.arrange_travel("Vijawayada","Singapore"))