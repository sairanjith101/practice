my_dict = {'apple': 3, 'banana': 2, 'orange': 1, 'grape': 4}

# Get the first two keys of the dictionary
keys_slice = list(my_dict.keys())[:2]
print(keys_slice)   # Output: ['apple', 'banana']

# Get the last two values of the dictionary
values_slice = list(my_dict.values())[-2:]
print(values_slice)   # Output: [1, 4]
