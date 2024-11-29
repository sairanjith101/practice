#Initialize matrix a  
a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ]  

# initialize variables to store the sums
col1_sum = 0
col3_sum = 0

# iterate through each row of the matrix
for row in a:
    # add the value in the first position to col1_sum
    col1_sum += row[0]
    
    # add the value in the third position to col3_sum
    col3_sum += row[2]

# print the results
print("Sum of first column:", col1_sum)
print("Sum of third column:", col3_sum)
