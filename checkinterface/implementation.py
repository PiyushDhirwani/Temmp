from checkinterface.abstract_class import AbstractClass

class Implementation(AbstractClass):
    def some_function(self, num1, num2):
        result = num1 + num2
        return str(result)
