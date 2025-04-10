from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, nums in enumerate(nums):
            complement = target - nums
            if complement in lookup:
                return [lookup[complement], i]
            lookup[nums] = i
# Example usage
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print("Output:", result)
