class Author:
    def __init__(self, name, bio=None):
        self.name = name
        self.bio = bio

    def __str__(self):
        return self.name


class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author  # Should be an Author object
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

    def borrow_book(self, book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            return f"{self.name} successfully borrowed {book.title}."
        return f"{book.title} is currently unavailable."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book)
            return f"{self.name} successfully returned {book.title}."
        return f"{self.name} did not borrow {book.title}."


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List of Book objects
        self.members = []  # List of Member objects

    def add_book(self, book):
        self.books.append(book)
        return f"Added {book.title} to the library."

    def add_member(self, member):
        self.members.append(member)
        return f"Added member {member.name} with ID {member.member_id}."

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_title):
        member = self.find_member(member_id)
        book = self.find_book(book_title)

        if not member:
            return f"No member found with ID {member_id}."
        if not book:
            return f"Book titled '{book_title}' not found in the library."

        return member.borrow_book(book)

    def return_book(self, member_id, book_title):
        member = self.find_member(member_id)
        book = self.find_book(book_title)

        if not member:
            return f"No member found with ID {member_id}."
        if not book:
            return f"Book titled '{book_title}' not found in the library."

        return member.return_book(book)

    def __str__(self):
        library_info = f"Library: {self.name}\nBooks:\n"
        for book in self.books:
            library_info += f"  {book} (Copies: {book.copies})\n"
        library_info += "Members:\n"
        for member in self.members:
            library_info += f"  {member}\n"
        return library_info


# Example usage
if __name__ == "__main__":
    # Create authors
    author1 = Author("J.K. Rowling")
    author2 = Author("George R.R. Martin")

    # Create books
    book1 = Book("Harry Potter and the Sorcerer's Stone", author1, copies=3)
    book2 = Book("A Game of Thrones", author2, copies=2)

    # Create library
    library = Library("City Library")

    # Add books to the library
    print(library.add_book(book1))
    print(library.add_book(book2))

    # Add members
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    print(library.add_member(member1))
    print(library.add_member(member2))

    # Borrow and return books
    print(library.borrow_book(1, "Harry Potter and the Sorcerer's Stone"))
    print(library.borrow_book(2, "Harry Potter and the Sorcerer's Stone"))
    print(library.borrow_book(2, "A Game of Thrones"))
    print(library.return_book(2, "A Game of Thrones"))
    print(library.borrow_book(2, "A Game of Thrones"))

    # Show library details
    print("\nCurrent Library Status:")
    print(library)
