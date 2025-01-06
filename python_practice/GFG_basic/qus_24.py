# Binary Array Sorting

arr = [1, 0, 1, 1, 0]
# arr = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]

class Solution:
    # Function to sort the binary array in non-decreasing order
    def binSort(self, arr):
        return sorted(arr)

sol = Solution()
print(sol.binSort(arr))