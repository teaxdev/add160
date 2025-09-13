from abc import ABC, abstractmethod

class Drink(ABC):
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor

    @abstractmethod
    def condiment(self):
        pass

    @abstractmethod
    def description(self):
        pass

class Coffee(Drink):
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def condiment(self):
        return "Creamer"

    def description(self):
        return f"Coffee: {self.size}, {self.flavor} flavor, with {self.condiment()}"
    
coffee = Coffee("Large", "Black")
print(coffee.description())

class Smoothie(Drink):
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def condiment(self):
        return "Strawberries"

    def description(self):
        return f"Coffee: {self.size}, {self.flavor} flavor, with {self.condiment()}"
    
smoothie = Smoothie("Medium", "Berry")
print(smoothie.description())