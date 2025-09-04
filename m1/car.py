# OOP Class and Instance Data

class ToyCar():
    
    toy_type = "car" # Class variable 

    def __init__(self, brand, color, car_type, motorized): # Instance variables
        self.brand = brand
        self.color = color
        self.car_type = car_type
        self.motorized = motorized
    
    def play(self): # "Play Feature" methods
        print("The toy car moves forward.")

    def sound(self):
        print("Vroom")
    
race_car = ToyCar("Hot Wheels", "red", "race car", True)
pickup_truck = ToyCar("Tonka", "yellow", "pickup truck", False)
police_car = ToyCar("Matchbox", "blue", "police car", True)

print(race_car.__class__) # Prints all of the required tests
print(race_car.__dict__)
race_car.play()
race_car.sound()