class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)
        result = []
        
        for i in range(0, n, k):
            result.extend(reversed(arr[i:i + k]))  # Reverse each group and append to result
            
        return result 

arr = [1, 2, 3, 4, 5]
k = 3

sol = Solution()
print(sol.reverseInGroups(arr, k))
