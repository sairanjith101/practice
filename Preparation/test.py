from itertools import combinations

nums = [3, 2, 4]
target = 6

class Solution:
    def findpair(self, nums, target):
        combination = combinations(nums, 2)
        for comb in combination:
            if sum(comb) == target:
                return comb

sol = Solution()
print(sol.findpair(nums,target))