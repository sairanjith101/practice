
# arr = [5, 5, 5, 5]

from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        return max(arr)

arr = [1, 8, 7, 56, 90]

sol = Solution()
print(sol.largest(arr))


# option 2

class Solution:
    def largest(self, arr):
        max_element = arr[0]
        for i in arr:
            if i > max_element:
                max_element = i
        return max_element

arr = [1, 8, 7, 56, 90]
sol = Solution()
print(sol.largest(arr))
