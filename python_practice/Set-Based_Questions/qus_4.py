# Remove duplicate elements from a list using a set.

from typing import List

nums = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(nums: List[int]) -> List[int]:
    nums = set(nums)
    return list(nums)

print(remove_duplicates(nums))