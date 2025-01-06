arr = [3, 2, 1, 56, 10000, 167]

class Solution:
    def get_min_max(self, arr):
        return min(arr), max(arr)
    
sol = Solution()
print(sol.get_min_max(arr))
    
