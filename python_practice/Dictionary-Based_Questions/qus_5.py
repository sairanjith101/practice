# Reverse a dictionary: Swap keys and values (assuming values are unique).

d = {'a': 1, 'b': 2, 'c': 3}

def reverse_dictionary(d: dict) -> dict:
    reverse_dict = {}
    for key,value in d.items():
        reverse_dict[value] = key
    return reverse_dict

print(reverse_dictionary(d))
