# 19. Factorial

n = 5

class Solution:
    def factorial (self, n):
        output = 1

        for i in range(1,n+1):
            output *= i
        
        return output

sol = Solution()
print(sol.factorial(n))