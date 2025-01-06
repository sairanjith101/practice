# First and Second Smallests

class Solution:
    def minAnd2ndMin(self, arr):
        output = []
        sorted_arr = sorted(arr)
        if sorted_arr[0] == sorted_arr[1]:
            return -1
        else:
            output.append(sorted_arr[0])
            output.append(sorted_arr[1])
        
        return output

# arr = [2, 4, 3, 5, 6]
arr = [2, 2, 2]

sol = Solution()
print(sol.minAnd2ndMin(arr))