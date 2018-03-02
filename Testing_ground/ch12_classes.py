# todo: add the Car class
class Car:
    
    def __init__(self, gl):
        # contains a gas attribute.
        self.gas_level = gl

    def __str__(self):
        return("This car has " + self.gas_level + " gallons of gas.")

    def get_gas_level(self):
        return(self.gas_level)

    def add_gas(self, amount):
        self.gas_level += amount

    def fill_up(self):
        uptocapacity = 0.0
        if self.gas_level <= 13.0:
            uptocapacity = 13.0 - self.gas_level
            self.add_gas(uptocapacity)
        else:
            uptocapacity = 0.0
        return(uptocapacity)

print(Car(float(input("Enter a number."))).fill_up())