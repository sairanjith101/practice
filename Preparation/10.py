# nums = [3, 4, 5, 2]
# nums = [1, 5, 4, 5]
nums = [10, 2, 5, 2]



class Solution:
    def findmaxproduct(self, nums):
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

            
sol = Solution()
print(sol.findmaxproduct(nums))