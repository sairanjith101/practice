# 15. First Occurence

txt = "GeeksForGeeks"
pat = "For"

class Solution:
    def firstOccurence(self, txt, pat):
        if pat in txt:
            return txt.find(pat)
        return -1

sol = Solution()
print(sol.firstOccurence(txt,pat))