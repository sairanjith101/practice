# Searching a number

k = 16
arr = [9, 7, 16, 16, 4]

# k=98
# arr = [1, 22, 57, 47, 34, 18, 66]


from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        output = []

        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1
        else:
            return -1

sol = Solution()
print(sol.search(k, arr))