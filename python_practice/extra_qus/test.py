class SuperMarket:

    name = "Sai Super Market"
    location = "Trichy"

    def __init__(self, customer):
        self.customer = customer

    def items(self, product, product_quantity):
        self.product = product
        self.product_quantity = product_quantity
        print(self.product)
        print(self.product_quantity)

obj = SuperMarket("Ranjith")
print(obj.name)
print(obj.location)
print(obj.customer)
obj.items("Milk", 1)
