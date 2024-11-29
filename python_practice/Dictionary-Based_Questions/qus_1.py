# Merge two dictionaries and sum the values of common keys

from collections import defaultdict
from typing import Dict

def merge_and_sum_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    # Using defaultdict to automatically handle missing keys with a default value of 0
    merged_dict = defaultdict(int)
    
    # Add all items from the first dictionary
    for key, value in dict1.items():
        merged_dict[key] += value
    
    # Add all items from the second dictionary
    for key, value in dict2.items():
        merged_dict[key] += value
    
    # Convert defaultdict back to a regular dict before returning
    return dict(merged_dict)

# Test cases
dict1 = {'a': 2, 'b': 4}
dict2 = {'b': 3, 'c': 5}

output = merge_and_sum_dicts(dict1, dict2)
print(output)  # Output: {'a': 2, 'b': 7, 'c': 5}

