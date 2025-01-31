d = {'a': 1, 'b': 2, 'c': 3}

def reverse_dictionary(d: dict) -> dict:
    reversed_dict = {}

    for key,value in d.items():
        reversed_dict[value] = key
    
    return reversed_dict

print(reverse_dictionary(d))