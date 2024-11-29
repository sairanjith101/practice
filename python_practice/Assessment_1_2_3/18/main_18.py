array1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
array2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

# Create a list of tuples containing elements from both arrays
zipped = list(zip(array2, array1))

# Sort the list of tuples based on the values from array2
sorted_tuples = sorted(zipped, key=lambda x: x[0])

# Extract the sorted elements from array1
sorted_array1 = [t[1] for t in sorted_tuples]

print(sorted_array1)
