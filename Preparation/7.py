nums = [1, 2, 2, 3, 4, 4, 5]

class Solution:
    def removedublicate(self, nums):
        return list(set(nums))
    
sol = Solution()
print(sol.removedublicate(nums))