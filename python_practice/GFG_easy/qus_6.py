
# arr = [5, 5, 5, 5]

from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        return max(arr)

arr = [1, 8, 7, 56, 90]

sol = Solution()
print(sol.largest(arr))