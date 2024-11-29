
class Solution:
    #Complete the below function
    def search(self,arr, x):

        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

arr = [1, 2, 3, 4]
x = 3

sol = Solution()
print(sol.search(arr,x))

