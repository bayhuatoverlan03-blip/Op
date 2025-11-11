class Appliance:
    def turn_on(self):
        print("The appliance is now on.")

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine starts washing clothes!")

a = Appliance()
w = WashingMachine()
a.turn_on()
w.turn_on()
