class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        head.append(x)
        return head

head =  [1,2,3,4,5]
x = 6

sol = Solution()
print(sol.insertAtEnd(head,x))

