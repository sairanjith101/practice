dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

class Solution:
    def mergetwodict(self,dict1,dict2):
        merged = dict1.copy()
        for key,value in dict2.items():
            if key in merged:
                merged[key] += value
            else:
                merged[key] = value
        return merged
        
sol = Solution()
print(sol.mergetwodict(dict1, dict2))