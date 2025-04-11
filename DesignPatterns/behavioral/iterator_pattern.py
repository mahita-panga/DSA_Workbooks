"""
Iterator Pattern: provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

#https://refactoring.guru/design-patterns/iterator

Great for situations where we need to provide a way to traverse through a collection of objects and also hide the underlying implementation.

Real World Analogy:
A good example is a radio: you can iterate through the different channels sequentially without knowing how the channels are stored or how the next channel is selected.

-> Iterator Class - provides the methods to iterate through the collection
-> Aggregate Class - provides the method to create an iterator

Example:
We have a Radio Station class and a Station class.
Stations are added to the Radio Station. We can iterate through the stations using an iterator.

"""
from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

#CONCRETE ITEM CLASS
class RadioStation:
    def __init__(self, frequency):
        self._frequency = frequency

    def get_frequency(self):
        return self._frequency

#AGGREGATOR CLASS
class StationList(Aggregate):
    def __init__(self):
        self._stations = []
        self._counter = 0

    def add_station(self, station):
        self._stations.append(station)

    def remove_station(self, station):
        self._stations.remove(station)

    def create_iterator(self):
        return self.StationIterator(self)

    # INNER CLASS IMPLEMENTING ITERATOR INTERFACE
    class StationIterator(Iterator):
        def __init__(self, station_list):
            self._station_list = station_list
            self._index = 0

        def has_next(self):
            return self._index < len(self._station_list._stations)

        def next(self):
            #CAR FM BEHAVIOR:⬇️
            # if self.has_next():
            #     station = self._station_list._stations[self._index]
            #     self._index += 1
            #     # Reset index if it's at the end of the collection
            #     if self._index == len(self._station_list._stations):
            #         self._index = 0
            #     return station
            # else:
            #     return None

            result = self._station_list._stations[self._index]
            self._index += 1
            return result

stations = StationList()
stations.add_station(RadioStation(89))
stations.add_station(RadioStation(101))
stations.add_station(RadioStation(102))
stations.add_station(RadioStation(103.2))

iterator = stations.create_iterator()

while iterator.has_next():
    print(iterator.next().get_frequency())

stations.add_station(RadioStation(95.1))
while iterator.has_next():
    print(iterator.next().get_frequency())