# Missing in Array

# arr = [1, 2, 3, 5]
# arr = [8, 2, 4, 5, 3, 7, 1]
arr = [1]
# arr = [2, 1]

# option 1
'''
class Solution:
    def missingNumber(self, arr):

        arr_set = set(arr)
        output = 0
        for i in range(1, max(arr) + 1):
            if i not in arr_set:
                output += i

        if len(arr) == 1 and arr[0] == 1:
            output += 2
        return output

sol = Solution()
print(sol.missingNumber(arr))

'''



# option 2


class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1
        total_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum


sol = Solution()
print(sol.missingNumber(arr))

