def subarray_sum_indexes(arr, target):
    start = 0
    current_sum = 0
    
    for end in range(len(arr)):
        # Add the current element to current_sum
        current_sum += arr[end]
        
        # Shrink the window as long as current_sum exceeds target
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        
        # Check if current_sum equals the target
        if current_sum == target:
            return [start + 1, end + 1]  # Convert to 1-based indexing
    
    return [-1]  # No valid subarray found

# Example usage:
print(subarray_sum_indexes([1, 2, 3, 7, 5], 12))  # Output: [2, 4]
print(subarray_sum_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))  # Output: [1, 5]
print(subarray_sum_indexes([5, 3, 4], 2))  # Output: [-1]
