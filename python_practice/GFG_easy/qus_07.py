# # s = "[{()}]"
# # s = "([]"
# # s = "([{]})"
# s = "[(])"

# class Solution:
#     def isBalanced(self, s):
#         n = len(s)
#         if n % 2 == 0:
#             return True
#         return False

# sol = Solution()
# print(sol.isBalanced(s))

# s = "[(])"
s = "[{()}]"

class Solution:
    def isBalanced(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():
                # It's an opening bracket
                stack.append(char)
            elif char in bracket_map:
                # It's a closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (optional, depending on problem statement)
                return False

        return not stack  # Stack should be empty if all brackets matched

    
sol = Solution()
print(sol.isBalanced(s))