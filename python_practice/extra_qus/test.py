class Solution:
    def findInt(self,arr):
        output = []
        for i in arr:
            if type(i) == int:
                output.append(i)
        return output

arr = [1, 2, 'a', 'b', '3', 'c', '4', 'd', 5]
sol = Solution()
print(sol.findInt(arr))