arr = [
    [1,2,3,4],
    [5,6,7,8],
    [1,2,3,4],
    [5,6,7,8]
]

column_2 = 1
column_4 = 1
for i in range(len(arr)):
    column_2 *= arr[i][1]
    column_4 *= arr[i][3]

print("Multiplication of second column : ", column_2)
print("Multiplication of second column : ", column_4)