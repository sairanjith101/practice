# Trapping Rain Water

# Water_Trapped[i]=min(Left_Max[i],Right_Max[i])−arr[i]

# arr = [3, 0, 1, 0, 4, 0, 2]
# arr = [3, 0, 2, 0, 4]
# arr = [1, 2, 3, 4]
arr = [2, 1, 5, 3, 1, 0, 4]

# Option 1

# class Solution:
#     def maxWater(self, arr):
#         output = []
#         for i in range(len(arr)):
#             if arr[i] == arr[0]:
#                 output.append(0)
            
#             if arr[i] != arr[0]:
#                 Left_Max = max(arr[:i+1])
#                 Right_Max = max(arr[i:])
                
#                 Water_Trapped = min(Left_Max,Right_Max) - arr[i]
#                 output.append(Water_Trapped)
        
#         return sum(output)


# sol = Solution()
# print(sol.maxWater(arr))

# Option 2

class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        # Step 1: Precompute Left_Max and Right_Max arrays
        Left_Max = [0] * n
        Right_Max = [0] * n
        
        Left_Max[0] = arr[0]
        for i in range(1, n):
            Left_Max[i] = max(Left_Max[i-1], arr[i])
        
        Right_Max[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            Right_Max[i] = max(Right_Max[i+1], arr[i])
        
        # Step 2: Calculate the water trapped at each index
        water_trapped = 0
        for i in range(n):
            water_trapped += min(Left_Max[i], Right_Max[i]) - arr[i]
        
        return water_trapped

# Test the solution
arr = [2, 1, 5, 3, 1, 0, 4]
sol = Solution()
print(sol.maxWater(arr))  # Output: 9
