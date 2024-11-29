import math

arr = [16, 6, 8, 4, 144]

perfect_sqr = []

for num in arr:
    if math.sqrt(num) == int(math.sqrt(num)):
        perfect_sqr.append(num)

print(perfect_sqr)
