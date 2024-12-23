# Third largest element

arr = [2, 4, 1, 3, 5]

# arr = [10, 2]

class Solution:
    def thirdLargest(self,arr):
        if len(arr) < 3:
            return -1
        new_arr = sorted(arr)
        return new_arr[-3]

sol = Solution()
print(sol.thirdLargest(arr))