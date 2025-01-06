arr1 = [10,20,30,40,60]
arr2 = [70,80,90,100,200]

output = 0

for i in range(len(arr1)):
    if i % 2 == 0:
        output += arr1[i]
    else:
        output += arr2[i]

print(output)