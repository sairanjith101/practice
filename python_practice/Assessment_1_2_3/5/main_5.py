arr = (1, 2, 'a', 'b', '3', 'c', '4', 'd', 5)

# create an empty list to store the filtered integers
integers = []

# iterate over each element in the original array
for element in arr:
    # check if the element is an integer
    if isinstance(element, int):
        # if it is, add it to the integers list
        integers.append(element)

# print the list of integers
print("Output : ", integers)
