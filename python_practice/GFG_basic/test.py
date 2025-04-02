class Solution:
    def reverstring(self, arr, k):
        box1 = []
        box2 = []
        for i in arr:
            if arr[i] > k:
                box1.append(i)
            else:
                box2.append(i)
        box2.reverse()
        box1.reverse()
        result = list[box1, box2]
        return result 


arr = [1, 2, 3, 4, 5]
k = 3

sol = Solution()
print(sol.reverstring(arr, k))