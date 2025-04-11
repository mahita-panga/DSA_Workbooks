"""
CORP -> an object to pass along a request to other objects in a chain until an object handles the request. This pattern decouples sender and receiver of a request based on type of request.
There is a flow associated with the object states
Ex: Bank Loan application
-> You apply for loan
-> Bank recieves request,
        validates request
        checks proofs submitted
        checks funds
        disburses the loan
        amount credited
        emi cut cut every month

TEMPLATE FOR CORP
"""

from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandler1(AbstractHandler):
    def handle(self, request):
        if request == "Request1":
            return "Handler1 handling request1"
        else:
            return super().handle(request)

class ConcreteHandler2(AbstractHandler):
    def handle(self, request):
        if request == "Request2":
            return "Handler2 handling request2"
        else:
            return super().handle(request)

def client_code(handler):
    for request in ["Request1", "Request2", "Request3"]:
        print(f"\nClient: Handling {request}")
        result = handler.handle(request)
        if result:
            print(f"  {result}")
        else:
            print(f"  {request} was not handled.")

handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()

handler1.set_next(handler2)

print("Chain: Handler1 > Handler2")
client_code(handler1)

print("\n")

print("Subchain: Handler2 only")
client_code(handler2)