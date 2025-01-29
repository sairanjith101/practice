array1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
array2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

sorted_arr = sorted(zip(array2,array1))

output = []

for pair in sorted_arr:
    output.append(pair[1])

print(output)