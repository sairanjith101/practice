arr = [16, 17, 4, 3, 5, 2]

class Solution:
    def leaders(self, arr):
        leaders = []
        max_right = arr[-1]
        leaders.append(max_right)

        for i in range(len(arr)-2, -1, -1):
            if arr[i] >= max_right:
                leaders.append(arr[i])
                max_right = arr[i]
        return leaders[::-1]

sol = Solution()
print(sol.leaders(arr))