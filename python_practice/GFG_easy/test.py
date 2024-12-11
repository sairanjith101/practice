arr = [15, 2, 45, 4, 7]
arr = [1]

class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        output = []

        for i in range(len(arr)):
            if arr[i] == i + 1:
                output.append(i + 1)

        return output
    
sol = Solution()
print(sol.valueEqualToIndex(arr))