class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):
            # Reverse each sub-array of size k
            arr[i:i + k] = reversed(arr[i:i + k])
        
        # Return the space-separated string
        return arr

# Input
k = 3
arr = [1, 2, 3, 4, 5]

# Create object and call the function
sol = Solution()
print(sol.reverseInGroups(arr, k))
