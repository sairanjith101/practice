from itertools import combinations

arr = [4, 4, 5, 3]
total = 8

comb = combinations(arr, 2)

count = 0

for com in comb:
    if sum(com) == total:
        count += 1

print(count)