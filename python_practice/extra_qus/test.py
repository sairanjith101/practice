arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

output = []

for i in range(len(arr)):
    row = []
    for j in range(len(arr)):
        row.append(arr[j][i])
    output.append(row)

print(output)