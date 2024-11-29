# Write a program to remove duplicates from a list while maintaining the order.


from typing import List


nums = [4, 5, 6, 4, 4, 7, 8, 6]
# nums = [1, 2, 2, 3, 1]

output = []

def remove_duplicates(nums: List[int]) -> List[int]:
    for n in nums:
        if n not in output:
            output.append(n)
    return output

print(remove_duplicates(nums))

