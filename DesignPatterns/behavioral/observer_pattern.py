"""
Observer Pattern: lets us define a subscription mechanism to notify multiple objects about any event that happens
to the object they are observing

Great for situations where a change to one object requires changing others, and you don't know how many objects need to be changed.
So all objects that needs to be changed will be subscribed to the subject and update its behaviour when the observing objects behaviour changes

Real World Analogy:
A good example is a job portal: when a company posts a new job listing,
all registered job seekers that have expressed interest in such a job are notified.

-> Publisher Class  - maintains the list of subscribers and notifies them when object state changes
-> Subscribers -> when it gets an update from publisher, does the action accordingly

Example:
    We have a JobPostings class and a JobSeeker class.
    JobSeekers register with JobPostings and are informed when a new job posting of their interest is available.
"""

from abc import ABC, abstractmethod

# OBSERVER INTERFACE
class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass

# PUBLISHER INTERFACE
class Publisher(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class JobSeeker(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, jobPostings):
        print(f'{self._name} received new job posting : {jobPostings.get_latest_job()}')

class JobPostings(Publisher):
    def __init__(self):
        self._observers = []
        self._jobs = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def add_job(self, job):
        self._jobs.append(job)
        self.notify()

    def get_latest_job(self):
        return self._jobs[-1] if self._jobs else None

johnDoe = JobSeeker('John Doe')
davidBrown = JobSeeker('David Brown')

jobPostings = JobPostings()
jobPostings.attach(johnDoe)
jobPostings.attach(davidBrown)

jobPostings.add_job('Software Engineer')
jobPostings.add_job('Staff Software Engineer')

jobPostings.detach(davidBrown)

jobPostings.add_job("CEO")
