# Second Largest

arr = [12, 35, 1, 10, 34, 1]
# arr = [10, 10, 10]
# arr = [10, 5, 10]

class Solution:
    def getSecondLargest(self, arr):
        if len(set(arr)) == 1:
            return -1
        
        new_set = set(arr)
        new_arr = list(sorted(new_set))
        second_largest = new_arr[-2]
        return second_largest

sol = Solution()
print(sol.getSecondLargest(arr))