# Prime Number

n = int(input("Enter a value: "))

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
    
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

sol = Solution()
print(sol.isPrime(n))