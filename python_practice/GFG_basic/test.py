# arr = [5, 24, 39, 60, 15, 28, 27, 40, 50, 90]
arr = [5, 10]


class Solution:
    def sumExceptFirstLast(self,arr):
        if len(arr) <= 2:
            return 0
        else:
            new_arr = arr[1:-1]
            output = 0
            for i in new_arr:
                output += i
            return output

sol = Solution()
print(sol.sumExceptFirstLast(arr))