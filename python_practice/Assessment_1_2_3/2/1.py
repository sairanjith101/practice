import itertools

arr1 = [-7, 1, 5, 1, 4]
total = 6

count = 0

combination = itertools.combinations(arr1, 2)

for comb in combination:
    print(comb)
    if total == sum(comb):
        count += 1

print("The Total count is : ", count)