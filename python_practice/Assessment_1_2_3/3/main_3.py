arr1 = (10, 20, 30, 40, 60)
arr2 = (70, 80, 90, 100, 200)

# Initialize the sum to zero
total = 0

# Iterate through both arrays simultaneously
for i in range(len(arr1)):
    # Check if the index is even for arr1 and odd for arr2
    if i % 2 == 0:
        total += arr1[i]
    else:
        total += arr2[i]

# Print the total sum
print(total)  # Output: 280
