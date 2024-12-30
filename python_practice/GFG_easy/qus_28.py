# Most Frequent Character

# s = "testsample"
s = "output"

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self, s):
        output = {}

        for i in s:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1

        max_freq = max(output.values())

        max_key = []

        for key,value in output.items():
            if value == max_freq:
                max_key.append(key)

        mfc = sorted(max_key)

        return mfc[0]

sol = Solution()
print(sol.getMaxOccurringChar(s))