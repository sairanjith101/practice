nums = [-1, -100, 3, 99]
k = 2

class Solution:
    def Rightrotate(self, nums, k):
        return nums[-k:] + nums[:-k]

sol = Solution()
print(sol.Rightrotate(nums, k))
