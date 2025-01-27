arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

coulmn_1 = 0
coulmn_2 = 1
coulmn_3 = 0
coulmn_4 = 1


for row in range(len(arr)):
    coulmn_1 += arr[row][0]
    coulmn_2 *= arr[row][1]
    coulmn_3 += arr[row][2]
    coulmn_4 *= arr[row][3]

print(coulmn_1)
print(coulmn_2)
print(coulmn_3)
print(coulmn_4)