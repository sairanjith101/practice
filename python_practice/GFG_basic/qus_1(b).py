class Solution:
    def seriesSum(self, n : int) -> int:
        return n*(n+1)//2
    
n = 5
sol = Solution()
print(sol.seriesSum(n))