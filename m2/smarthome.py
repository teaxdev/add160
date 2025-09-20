# OOP 2.8 Inheritance vs Composition

class Device():

    def __init__(self, name, status, power):
        self.name = name
        self.status = status
        self.power = power

    # def status(self):
    #     return self.name, self.power
    
    # def power(self, value):
    #     self.power = value

class Light(Device):
    def __init__(self, name, status, power, brightness):
        super().__init__(name, status, power)
        self.brightness = brightness

    # def brightness(self, value):
    #     self.brightness = value

class LEDLight(Light):
    def __init__(self, name, status, power, brightness, color):
        super().__init__(name, status, power, brightness)
        self.color = color

class SmartBulb(Light):
    def __init__(self, name, status, power, brightness, energy):
        super().__init__(name, status, power, brightness)
        self.energy = energy

class Thermostat(Device):
    def __init__(self, name, status, power, temp, target_temp):
        super().__init__(name, status, power)
        self.temp = temp
        self.target_temp = target_temp

class SmartHome():
    def __init__(self):
        # self.choose_dev = choose_dev
        # self.action = action
        self.led = LEDLight("LEDLight", "yes", "Off", 75, "red")
        self.smart = SmartBulb("Smart Bulb", "yes", "Off", 75, "red")
        self.thermo = Thermostat("Thermostat", "yes", "Off", "75", 68)

    def choose_dev(self):
        while True:
            # return f"Power {self.led.power}"
            print(f"Devices: \n1. {self.led.name} - Status: {self.led.power}, Brightness: {self.led.brightness} ")
            print(f"2. {self.smart.name} - Status: {self.smart.power}")
            print(f"3. {self.thermo.name} - Status: {self.thermo.power}, Current Temperature: {self.thermo.temp}, Target Temperature: {self.thermo.target_temp}\n")

            if self.led.power == "Off":
                print(f"Turn LED On")
            else:
                print(f"Turn LED Off")

            if self.led.brightness > 50:
                print(f"Set LED Brightness to 50%")
            else:
                print(f"Set LED Brightness to 80%")

            if self.smart.power == "Off":
                print(f"Turn Smart Bulb On")
            else:
                print(f"Turn Smart Bulb Off")

            if self.thermo.target_temp > 70:
                print(f"Set LED target brightness to 68")
            else:
                print(f"Set LED target brightness to 72")
            act = input("Input action: ")

            if self.led.power == "Off" and act == "1":
                self.led.power = "On"
                print(f"LED Light turned on.\n")
            elif act == "1":
                self.led.power = "Off"
                print(f"LED Light turned off.\n")

            elif self.led.brightness > 50 and act == "2":
                self.led.brightness = 50
                print(f"Brightness set to 50.\n")
            elif act == "2":
                self.led.brightness = 80
                print(f"Brightness set to 80.\n")
            
            elif self.smart.power == "Off" and act == "3":
                self.smart.power = "On"
                print(f"Smart Bulb turned on.\n")
            elif act == "3":
                self.smart.power = "Off"
                print(f"Smart Bulb turned off.\n")

            elif self.thermo.target_temp > 70 and act == "4":
                self.thermo.target_temp = 68
                print(f"Target Temp set to 68.\n")
            elif act == "4":
                self.thermo.target_temp = 72
                print(f"Target Temp set to 72.\n")

            elif act == "5":
                print("Exiting SmartHome")
                break

            else:
                print("Please input a valid action\n")


        # dev = input()
        # if dev == 1:
        #     print("choose an action 1. 2. 3.")

        #     act = input()
        #     if act == 1:
        #         print("LED Light turned off")
        # if dev == 2:
        #     print("choose an action 1. 2. 3.")
        #     act = input()
        # if dev == 3:
        #     print("choose an action 1. 2. 3.")
        #     act = input()

home = SmartHome()
home.choose_dev()