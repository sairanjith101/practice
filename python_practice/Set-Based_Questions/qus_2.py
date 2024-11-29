# Find the difference between two sets.

from typing import Tuple

set1 = {1, 2, 3}
set2 = {3, 4, 5}

def find_set_difference(set1: set, set2: set) -> Tuple[set, set]:
    diff_set_1 = set.difference(set1,set2)
    diff_set_2 = set.difference(set2,set1)
    return diff_set_1,diff_set_2

diff_set_1, diff_set_2 = find_set_difference(set1,set2)
print("Difference (set1 - set2): ", diff_set_1)
print("Difference (set2 - set1): ", diff_set_2)