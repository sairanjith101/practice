# Array Leaders

# not learn

def find_leaders(arr):
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)

    # Traverse from second last element to the left
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    
    return leaders[::-1]  # Reverse to maintain correct order

# Example test cases
print(find_leaders([16, 17, 4, 3, 5, 2]))  # Output: [17, 5, 2]
print(find_leaders([10, 4, 2, 4, 1]))  # Output: [10, 4, 4, 1]
print(find_leaders([5, 10, 20, 40]))  # Output: [40]
print(find_leaders([30, 10, 10, 5]))  # Output: [30, 10, 10, 5]
