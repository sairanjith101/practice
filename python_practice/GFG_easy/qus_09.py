class Solution:
    def findTwoElement( self,arr):
        repeat_num = []
        positive_num = []
        dict = {} 
        for i in range(1, max(arr)):
            if i not in arr:
                positive_num.append(i)
        for j in arr:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
        output = dict.values()
        repeat_num.append(max(output))
        return repeat_num, positive_num

arr = [2, 2]
sol = Solution()
print(sol.findTwoElement(arr))