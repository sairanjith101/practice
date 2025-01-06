arr = [1, 2, 3, 4, 5]

class Solution:
    def rotate(self, arr):
        last_element = arr.pop()
        arr.insert(0, last_element)
        return arr
    
sol = Solution()
print(sol.rotate(arr))