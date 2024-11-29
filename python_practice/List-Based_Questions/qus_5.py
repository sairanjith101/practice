# Write a program to find the intersection of multiple lists.

from typing import List
from collections import Counter

def intersection_of_lists(lists: List[List[int]]) -> List[int]:
    # Flatten the lists into one list
    all_elements = []
    for sublist in lists:
        for elem in sublist:
            all_elements.append(elem)
    
    # Count occurrences of each element in the flattened list
    counts = Counter(all_elements)
    
    # The intersection will include elements that appear in all lists
    num_lists = len(lists)

    intersection = []
    for elem, count in counts.items():
        if count == num_lists:
            intersection.append(elem)  # Append the element itself, not the count
    
    return intersection

# Test cases
lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# lists = [[10, 20, 30], [20, 30], [30, 40]]

print(intersection_of_lists(lists))




