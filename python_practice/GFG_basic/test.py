from collections import Counter

arr1=[1,2,3,4,5]
arr2=[1,2,3,4,6]

class Solution:
    def isarrayequal(self,arr1, arr2):
        a = Counter(arr1)
        b = Counter(arr2)
        if a == b:
            return True
        return False

sol = Solution()
print(sol.isarrayequal(arr1,arr2))