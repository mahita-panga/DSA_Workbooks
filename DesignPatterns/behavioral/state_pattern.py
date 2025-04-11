"""
In this pattern, objects can alter its behaviour whenver there is a change
 in internal state and behave like a different class.
Like "multi-personality disorder" but in objects🤡

State pattern suggests that we create new classes for all possible states of an object and extract all state-specific behaviors into these classes.

REAL WORLD ANALOGY:
The buttons and switches in your smartphone behave differently depending on the current state of the device:
    When the phone is unlocked, pressing buttons leads to executing various functions.
    When the phone is locked, pressing any button leads to the unlock screen.
    When the phone’s charge is low, pressing any button shows the charging screen.

Ex:
Imagine that we have a Document class. A document can be in one of three states: Draft, Moderation and Published. The publish method of the document works a little bit differently in each state:

In Draft, it moves the document to moderation.
In Moderation, it makes the document public, but only if the current user is an administrator.
In Published, it doesn’t do anything at all.
"""
from abc import ABC, abstractmethod

#STATE INTERFACE
class DocumentState(ABC):
    @abstractmethod
    def render(self, doc, user):
        pass

    @abstractmethod
    def publish(self, doc, user):
        pass

#Multiple states
class Draft(DocumentState):
    def render(self, doc, user):
        if user.is_admin() or user.is_author():
            # Implement the logic to render the document
            pass

    def publish(self, doc, user):
        if user.is_admin():
            print("MOVING DRAFT TO MODERATION")
            doc.state = Moderation()

class Moderation(DocumentState):
    def render(self, doc, user):
        if user.is_admin() or user.is_author():
            # Implement the logic to render the document
            pass

    def publish(self, doc, user):
        if user.is_admin():
            print("NOW MOVING MODERATION TO PUBLISHING THE DOCUMENT")
            doc.state = Published()

class Published(DocumentState):
    def render(self, doc, user):
        if user.is_admin() or user.is_author():
            # Implement the logic to render the document
            pass

    def publish(self, doc, user):
        print("PUBLISHED DOCUMENT BY USER")
        pass

class Document:
    def __init__(self):
        self.state = Draft()

    def render(self, user):
        self.state.render(self, user)

    def publish(self, user):
        self.state.publish(self, user)

class User:
    def __init__(self,role):
        self.role = role
    def is_admin(self):
        # Implement the logic to check if the user is an admin
        if self.role == 'admin':
            return True
        return False

    def is_author(self):
        # Implement the logic to check if the user is the author of the document
        if self.role == 'author':
            return True
        return False

admin_user = User('admin')
newdoc = Document()
newdoc.publish(user=admin_user)
newdoc.publish(user=admin_user)
newdoc.publish(user=admin_user)
newdoc.publish(user=admin_user)


