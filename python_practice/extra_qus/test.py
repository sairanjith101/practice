class Solution:
    def factorialnum(self,n):
        box = 1
        for i in range(1, n+1):
            box *= i
        return box
n = int(input("Enter a value: "))
sol = Solution()
print(sol.factorialnum(n))