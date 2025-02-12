class vehicle:

    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def display(self):
        print(self.brand)
        print(self.year)

class Truck(vehicle):

    def __init__(self, brand, year, tank, load):
        self.tank = tank
        self.load = load

        vehicle.__init__(self,brand,year)

    def details(self):
        print(f'Brand: {self.brand}')
        print(f'Year: {self.year}')
        print(f'Tank: {self.tank}')
        print(f'Load: {self.load}')

obj = Truck('TATA', 2018, "20L", '200T')
obj.display()
obj.details()