arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

sum_1 = 0
sum_3 = 0

for i in range(len(arr)):
    sum_1 += arr[i][0]
    sum_3 += arr[i][2]

print(sum_1)
print(sum_3)

mul_2 = 1
mul_4 = 1

for i in range(len(arr)):
    mul_2 *= arr[i][1]
    mul_4 *= arr[i][3]

print(mul_2)
print(mul_4)