class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            print("Enter a positive number")
        
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
        
n = int(input("Enter a value: "))
sol = Solution()
print(sol.isPrime(n))