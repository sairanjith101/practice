# Write a program to find the union and intersection of two sets.

from typing import Tuple

def find_union_and_intersection(set1: set, set2: set) -> Tuple[set, set]:
    union_set = set.union(set1, set2)  # Find the union
    intersection_set = set.intersection(set1, set2)  # Find the intersection
    return union_set, intersection_set  # Return as a tuple

# Test case
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union, intersection = find_union_and_intersection(set1, set2)
print(f"Union: {union}, Intersection: {intersection}")
