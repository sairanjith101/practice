class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        fib_ser = []
        a,b = 1,1
        for i in range(n):
            fib_ser.append(a)
            a,b = b, a + b
        return fib_ser

n = 2
sol = Solution()
print(sol.printFibb(n))