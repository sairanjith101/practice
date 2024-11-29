import math

arr = (16, 6, 8, 4, 144)
perfect_squares = []

for num in arr:
    if math.sqrt(num) == int(math.sqrt(num)):
        perfect_squares.append(num)

print(perfect_squares)
