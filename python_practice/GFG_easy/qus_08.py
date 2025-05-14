# find equilibrium

# arr = [1, 2, 0, 3]
# arr = [1, 1, 1, 1]
arr = [-7, 1, 5, 2, -4, 3, 0]


class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        for i in range(len(arr)):
            box_1 = arr[:i]
            box_2 = arr[i+1:]
            if sum(box_1) == sum(box_2):
                return i
        return -1

sol = Solution()
print(sol.findEquilibrium(arr))