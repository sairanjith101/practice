class Solution:
    def seriesSum(self, n : int) -> int:
        output = 0

        for i in range(n+1):
            output += i
        
        return output

n = 5   
sol = Solution()
print(sol.seriesSum(n))