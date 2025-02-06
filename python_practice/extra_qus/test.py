class Solution:
    def findFactors(self,n):
        output = []
        for i in range(1, n+1):
            if n % i == 0:
                output.append(i)
        return output
    
n = int(input("Enter a value: "))
sol = Solution()
print(sol.findFactors(n))