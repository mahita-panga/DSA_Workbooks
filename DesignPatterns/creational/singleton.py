"""

SINGLETON PATTERN:
    Ensures a class has only one instance and provides global access of this class instance whenever a
    new class object is instantiated

-> Used for creating Logging class, configuration class or db connection. This ensures we are not creating
new instances of the connections in our application

"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__new__(cls)

        return cls._instance



obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2) #should print True

##THREAD SAFE SINGLETON IMPLEMENTATION
"""
The original Singleton implementation is not thread-safe. 
If multiple threads try to create an instance at the same time, 
they might end up creating multiple instances, which defeats the purpose of a Singleton. 
To make it thread-safe, we'll need to use a locking mechanism to ensure that only one thread can enter the section of code that creates the instance.
"""

import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

def worker():
    singleton = Singleton()
    print(f"Singleton instance ID is: {id(singleton)} for {threading.current_thread().name}")

for i in range(10):
    threading.Thread(target=worker, name=f'Thread {i}').start() #ONLY ONE OBJECT IS CREATED IN ALL WORKERS

