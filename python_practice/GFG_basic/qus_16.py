# Immediate Smaller Element

arr = [4, 2, 1, 5, 3]
# arr = [5, 6, 2, 3, 1, 7]
# arr = [4, 1]

class Solution:
    def immediateSmaller(self,arr):
        smaller = []

        for i in range(len(arr)):
            if i < len(arr) - 1 and arr[i] > arr[i+1]:
                smaller.append(arr[i+1])
            else:
                smaller.append(-1)
        
        return smaller
    
sol = Solution()
print(sol.immediateSmaller(arr))