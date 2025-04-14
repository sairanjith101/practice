from collections import Counter

nums = [1, 2, 2, 3, 1, 4, 2]

class Solution:
    def frequencyofnumber(self,nums):
        return Counter(nums)
       
sol = Solution()
print(sol.frequencyofnumber(nums))