# s = "leetcode"
s = "loveleetcode"
# s = "aabb"

class Solution:
    def firstnonrepeat(self, s):
        box = {}
        for i in s:
            if i not in box:
                box[i] = 1
            else:
                box[i] += 1
        # for key,value in box.items():
        #     if value == 1:
        #         return key
        for idx,char in enumerate(s):
            if box[char] == 1:
                return idx
        return -1
    
sol = Solution()
print(sol.firstnonrepeat(s))