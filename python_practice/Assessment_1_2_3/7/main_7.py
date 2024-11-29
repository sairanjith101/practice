arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

# initialize variables to store the sums
col1_sum = 0
col3_sum = 0

# iterate through each row of the matrix
for cols in arr:
    # add the value in the first position to col1_sum
    col1_sum += cols[0]
    
    # add the value in the third position to col3_sum
    col3_sum += cols[2]

# print the results
print("Sum of first column:", col1_sum)
print("Sum of third column:", col3_sum)

# initialize variables to store the multi
column_2 = 1
column_4 = 1

# iterate through each row of the matrix
for i in range(len(arr)):
    # mul the value in the second position to column_2
    column_2 *= arr[i][1]
    # mul the value in the fourth position to column_4
    column_4 *= arr[i][3]

print("Multiplication of second column : ", column_2)
print("Multiplication of fourth column : ", column_4)