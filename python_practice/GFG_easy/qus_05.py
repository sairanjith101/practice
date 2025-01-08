arr = [0, 1, 2, 0, 1, 2]
# arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        arr.sort()
        return arr

sol = Solution()
print(sol.sort012(arr))
