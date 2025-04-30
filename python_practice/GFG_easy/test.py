class Solution:
    def findTwoElement(self, arr): 
        missing_num = -1
        repating_num = -1
        dict = {}
        
        # Build the dictionary to count occurrences of each element
        for i in arr:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        # Find the repeating number (with count > 1)
        max_value = max(dict.values())
        for key, value in dict.items():
            if value == max_value:
                repating_num = key  # Store the repeating number
        
        # Find the missing number (from 1 to n)
        for i in range(min(arr), max(arr)+1):
            if i not in dict:
                missing_num = i  # Assign the missing number
        
        return [repating_num, missing_num]

# Test case
arr = [4, 3, 6, 2, 1, 1]
sol = Solution()
print(sol.findTwoElement(arr))  # Output: [1, 5]
