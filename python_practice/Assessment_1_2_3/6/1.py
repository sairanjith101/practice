arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

total = 0

for i in range(len(arr)):
    total += arr[i][i]

print(total)