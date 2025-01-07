# Array Duplicates

arr = [2, 3, 1, 2, 3]
# arr = [0, 3, 1, 2]

class Solution:
    def findDuplicates(self, arr):
        seen = set()
        duplicate = set()

        for num in arr:
            if num in seen:
                duplicate.add(num)
            else:
                seen.add(num)
        return list(duplicate)

sol = Solution()
print(sol.findDuplicates(arr))