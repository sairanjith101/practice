# 🚗 Vehicle Hierarchy in Python

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        Vehicle.__init__(self, brand, model)
        self.bike_type = bike_type
    
    def display_info(self):
        Vehicle.display_info(self)
        print(f"Bike Type: {self.bike_type}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        Vehicle.__init__(self, brand,model)
        self.num_doors = num_doors

    def display_info(self):
        Vehicle.display_info(self)
        print(f"Number of Doors: {self.num_doors}")

bike = Bike("TVS", "Splinder", "Commercial")
print("\n---Bike Info---")
bike.display_info()

car = Car("Maruti", "Swift", 4)
print("\n---Car Info---")
car.display_info()