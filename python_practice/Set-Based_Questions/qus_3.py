# Check if one set is a subset of another.

from typing import Tuple

# set1 = {1, 2}
# set2 = {1, 2, 3}

# set1 = {4, 5, 6}
# set2 = {4, 5, 6}

set1 = {7, 8}
set2 = {9, 10}

def check_subset(set1: set, set2: set) -> Tuple[bool, bool]:
    subset_1 = set.issubset(set1,set2)
    subset_2 = set.issubset(set2,set1)
    return subset_1,subset_2

subset_1, subset_2 = check_subset(set1,set2)
print(subset_1,subset_2)