class Solution:
    def rotate(self, arr):
        new_arr = arr[-1:] + arr[0:-1]
        return new_arr
    
arr = [1, 2, 3, 4, 5]
sol = Solution()
print(sol.rotate(arr))