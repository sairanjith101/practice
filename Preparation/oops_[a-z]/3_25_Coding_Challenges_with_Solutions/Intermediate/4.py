class Book:
    inventory = []

    def __init__(self, book_id, title, author, price, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        Book.inventory.append(self)

    def display_details(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Price: ₹{self.price}, Quantity: {self.quantity}")

    def update_quantity(self, qty):
        self.quantity += qty
        print(f"Updated quantity of '{self.title}' to {self.quantity}")

    def sell_book(self, qty):
        if self.quantity >= qty:
            self.quantity -= qty
            print(f"Sold {qty} copy/copies of '{self.title}'")
        else:
            print(f"Not enough stock to sell {qty} copy/copies of '{self.title}'")

    @classmethod
    def show_inventory(cls):
        print("\n--- Book Inventory ---")
        for book in cls.inventory:
            book.display_details()


# Demo / Testing
b1 = Book(101, "Python Basics", "John Smith", 450, 10)
b2 = Book(102, "Advanced Python", "Jane Doe", 650, 5)
b3 = Book(103, "Data Structures", "Alan Turing", 500, 8)

Book.show_inventory()

b1.sell_book(3)
b2.update_quantity(2)

Book.show_inventory()
