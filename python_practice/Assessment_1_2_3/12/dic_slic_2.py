my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Convert the dictionary into a list of key-value tuples
my_list = list(my_dict.items())

# Slice the list
sliced_list = my_list[1:4]

# Convert the sliced list back into a dictionary
sliced_dict = dict(sliced_list)

print(sliced_dict)  # Output: {'b': 2, 'c': 3, 'd': 4}
