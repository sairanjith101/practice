s = "loveleetcode"

class Solution:
    def firstnonrepeatingchar(self, s):
        box = {}
        for i in s:
            if i not in box:
                box[i] = 1
            else:
                box[i] += 1
        print(box)
        for i in s:
            if box[i] == 1:
                return i
        return None

sol = Solution()
print(sol.firstnonrepeatingchar(s))