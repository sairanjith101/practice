arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

diagonal_sum = 0

for i in range(len(arr)):
    diagonal_sum += arr[i][i]

print(diagonal_sum)
