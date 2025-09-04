class Dog:
    def __init__(self, average_weight, height_range, life_span, color):
        self.average_weight = average_weight
        self.height_range = height_range
        self.life_span = life_span
        self.color = color

class HerdingDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, herding_ability):
        super().__init__(average_weight, height_range, life_span, color)
        self.herding_ability = herding_ability

    def herd(self):
        return "This dog is herding sheep!"
    
class ToyDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, barking_ability):
        super().__init__(average_weight, height_range, life_span, color)
        self.barking_ability = barking_ability

    def bark(self):
        return "This dog is barking at nothing half the time"
    
class TerrierDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, high_energy):
        super().__init__(average_weight, height_range, life_span, color)
        self.high_energy = high_energy

    def run(self):
        return "This dog will run around all day"

if __name__ == "__main__":
    collie = HerdingDog(average_weight=60, height_range="22-26 inches", life_span="12-14 years", color="various", herding_ability="excellent")
    print(f"Collie: {collie.herd()}")

if __name__ == "__main__":
    chihuahua = ToyDog(average_weight=5, height_range="6-9 inches", life_span="12-20 years", color="various", barking_ability="supreme")
    print(f"Chihuahua: {chihuahua.bark()}")

if __name__ == "__main__":
    bull = TerrierDog(average_weight=60, height_range="22-26 inches", life_span="12-14 years", color="various", high_energy="yes")
    print(f"Bull: {bull.run()}")