# Create a list of all unique elements from two lists.

from typing import List

# list1 = [1, 2, 3]
# list2 = [2, 3, 4]

list1 = [4, 5, 6]
list2 = [6, 7, 8]

def union_of_lists(list1: List[int], list2: List[int]) -> List[int]:
    list1 = set(list1)
    list2 = set(list2)
    unique = set.union(list1,list2)
    return list(unique)

print(union_of_lists(list1,list2))