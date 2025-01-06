# Rotating an Array

arr = [-1, -2, -3, 4, 5, 6, 7]
d = 2

# arr = [1, 3, 4, 2]
# d = 3

class Solution:
    def leftRotate(self, arr, d):
        new_arr = arr[d:] + arr[:d]
        return new_arr

sol = Solution()
print(sol.leftRotate(arr,d))