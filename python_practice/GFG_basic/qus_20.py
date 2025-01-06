# 20. Count Squares

n = 9

class Solution:
    def countSquares(self, n):
        output = 0

        for i in range(1, n):
            per_sqr =  i ** 2
            if per_sqr < n:
                output += 1
        return output

sol = Solution()
print(sol.countSquares(n))

# Options 2

import math

class Solution:
    def countSquares(self, n):
        # Use math.sqrt and int() to count perfect squares less than n
        return int(math.sqrt(n - 1))

sol = Solution()
# Test cases
print(sol.countSquares(9))  # Output: 2
print(sol.countSquares(3))  # Output: 1
print(sol.countSquares(5))  # Output: 2
