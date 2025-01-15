arr = [3, 0, 1, 0, 4, 0, 2]

for i in range(len(arr)):
    n = arr[i:] + arr[:i]
    print(n)