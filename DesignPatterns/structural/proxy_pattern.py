"""
Proxy Pattern -> used when we want to control access to another object by creating a surrogate or placeholder object called "PROXY".

Proxy has the same interface as the original object.

Proxy can add extra functionality like lazy loading, access control, logging, caching, etc., without changing the original object.

-> https://refactoring.guru/design-patterns/proxy

Analogy:
Think of a security guard (Proxy) outside a building (Real Object).
You can't directly enter the building; the guard checks your ID and grants/denies access based on certain rules.
Here, the Security Guard (Proxy) controls the access to Building (Real Object).
The building’s internal functioning doesn't change, and the security guard doesn't need to know the internals of the building.

Scenario:
Used when we want to add a layer of control around accessing an object like lazy initialization, access control, logging, etc., without modifying the actual object.

"""

from abc import ABC, abstractmethod


#INTERFACE
class Building(ABC):
    @abstractmethod
    def enter(self, person_name):
        pass


#REAL SUBJECT
class OfficeBuilding(Building):
    def enter(self, person_name):
        return f"{person_name} entered the office building 🏢"


#PROXY
class SecurityGuardProxy(Building):
    def __init__(self):
        self._building = OfficeBuilding()
        self._allowed_people = {"Alice", "Bob", "Charlie"}

    def enter(self, person_name):
        if person_name in self._allowed_people:
            return self._building.enter(person_name)
        else:
            return f"Access Denied 🚫 for {person_name}"


#USAGE/CLIENT
security = SecurityGuardProxy()

print(security.enter("Alice"))  # Allowed
print(security.enter("Eve"))  # Access Denied
print(security.enter("Charlie"))  # Allowed
