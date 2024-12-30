# Sort The Array

# option 1

'''
arr = [1, 5, 3, 2]

class Solution:
    def sortArr(self, arr):
        return sorted(arr)

sol = Solution()
print(sol.sortArr(arr))
'''

# option 2

class Solution:
    def sortArr(self, arr):
        return sorted(arr)
        
user = input("Enter a element: ")
arr = list(map(int, user.split()))

sol = Solution()
print(sol.sortArr(arr))
