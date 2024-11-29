arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

diagonal = 0

for a in range(len(arr)):
    diagonal += a[i][i]

column_1 = 0
column_3 = 0

for i in arr:
    column_1 += i[0]
    column_3 += i[2]

print("Sum of column 1 : ", column_1)
print("Sum of column 1 : ", column_3)

column_2 = 1
column_4 = 1

for i in range(len(arr)):
    column_2 *= arr[i][1]
    column_4 *= arr[i][3]

print("Multiple of column 2 : ", column_2)
print("Multiple of column 2 : ", column_4)