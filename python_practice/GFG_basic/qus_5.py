from collections import Counter

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        #code here
        return Counter(arr1) == Counter(arr2)

arr1 = [1, 2, 5, 4, 0]
arr2 = [2, 4, 5, 0, 1]
sol =Solution()
print(sol.check(arr1,arr2))
