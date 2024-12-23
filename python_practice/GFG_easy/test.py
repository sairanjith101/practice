k = 16
arr = [9, 7, 16, 16, 4]

def search(k, arr):
    for i in range(len(arr)):
        if arr[i] == k:
            return i+1
    else:
        return -1

print(search(k, arr))