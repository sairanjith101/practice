# Find the most frequent element in a list using a dictionary or collections.Counter.

from collections import Counter
from typing import List

def most_frequent(nums: List[int]) -> int:
    # Use Counter to count occurrences of each element
    count = Counter(nums)
    # Find the key with the maximum frequency
    output = max(count, key=count.get)
    return output

# Test case
nums = [1, 3, 2, 3, 1, 3]
print(most_frequent(nums))  # Output: 3

