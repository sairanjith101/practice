k = 3
arr= [1, 2, 3, 4, 5]

# k = 5
# arr = [5, 6, 8, 9]

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):

        if len(arr) > k:
            group_1 = list(reversed(arr[:k]))
            group_2 = list(reversed(arr[k:]))
            group = group_1 + group_2
        else:
            group = list(reversed(arr))
        
        return ' '.join(map(str, group))
    
sol = Solution()
print(sol.reverseInGroups(arr,k))