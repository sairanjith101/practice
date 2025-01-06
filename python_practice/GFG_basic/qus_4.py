class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        rev_str = s[::-1]
        return rev_str

s = "Geeks"     
sol = Solution()
print(sol.reverseString(s))