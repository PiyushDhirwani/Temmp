from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def do_something_else(self):
        pass