from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution:
    def findanagram(self, words):
        box = defaultdict(list)
        for w in words:
            key = ''.join(sorted(w))
            box[key].append(w)
        return list(box.values())
    
sol = Solution()
print(sol.findanagram(words))