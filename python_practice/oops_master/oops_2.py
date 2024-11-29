class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive value.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive value.")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = value
        self._width = value

    def __str__(self):
        return f"Square(side_length={self.width})"


# Example usage
rect = Rectangle(4, 5)
print(rect)  # Rectangle(width=4, height=5)
print("Area:", rect.area())  # Area: 20
print("Perimeter:", rect.perimeter())  # Perimeter: 18

square = Square(4)
print(square)  # Square(side_length=4)
print("Area:", square.area())  # Area: 16
print("Perimeter:", square.perimeter())  # Perimeter: 16

# Update square side length
square.width = 6
print(square)  # Square(side_length=6)
