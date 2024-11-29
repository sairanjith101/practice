class Product:
    def __init__(self,name,price,quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name} - Rs.{self.price} x {self.quantity}"
    
class Order:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.total_price() for product in self.products)
    
    def __str__(self):
        product_list = "\n".join(str(product) for product in self.products)
        total_cost = self.calculate_total()
        return f"Order Details:\n{product_list}\nTotal Cost: Rs.{total_cost:.2f}"
    
if __name__ == "__main__":
    product1 = Product(name="Laptop", price=1200, quantity=1)
    product2 = Product(name="Mouse", price=400, quantity=1)
    product3 = Product(name="Keyboard", price=200, quantity=1)

    order = Order()
    order.add_product(product1)
    order.add_product(product2)
    order.add_product(product3)

    print(order)