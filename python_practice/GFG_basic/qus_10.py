arr = [1, 2, 3, 4, 6]
k = 6

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        for i in arr:
            if i == k:
                return True
        return False
            
sol = Solution()
print(sol.searchInSorted(arr, k))