# Max Min

# N = 4
# A  = [1, 3, 4, 1]

class Solution:
    def findSum(self, A, N): 
        if len(A) != N:
            return "Length of the array does not match N"
        
        min_value = min(A)
        max_value = max(A)
        return min_value + max_value

N = 5
A = [-2, 1, -4, 5, 3]

sol = Solution()
print(sol.findSum(A, N))
