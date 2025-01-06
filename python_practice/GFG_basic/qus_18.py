# 18. Sum of first n terms

class Solution:
    def sumOfSeries(self,n):
        output = 0
        for i in range(1,n+1):
            nth_term = i ** 3
            output += nth_term
        return output

n = 7
sol = Solution()
print(sol.sumOfSeries(n))