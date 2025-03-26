class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here

        a = list(set(a))
        b = list(set(b))

        output = []

        for j in b:
            if j not in a:
                output.append(j)

        if not output:
            return True
        else:
            return False

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

sol = Solution()
print(sol.isSubset(a,b))



# Option 2

class Solution:
    def checksubset(self, a, b):
        for i in b:
            if i not in a:
                return False
        return True


a=[11,7,13,21,3,7,3]
b=[11,3,7,1,7]
sol = Solution()
print(sol.checksubset(a,b))