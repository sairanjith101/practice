import math

arr = [16, 6, 8, 4, 144]

output = []

for i in arr:
    sqr_value = math.sqrt(i)
    if i % sqr_value == 0:
        output.append(i)

print(output)