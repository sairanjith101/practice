# he string x in the string s.
class Solution:
    def firstOccurence(self, txt, pat):
        if pat in txt:
            for i, char in enumerate(txt):
                split_pat = list(pat)
                if split_pat[0] == char:
                    return i
        return -1

txt = "GeeksForGeeks"
pat = "Fr"
sol = Solution()
print(sol.firstOccurence(txt,pat))