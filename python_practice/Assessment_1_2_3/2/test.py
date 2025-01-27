from itertools import combinations

# arr = [4, 4, 5, 3]
# value = 8

arr = [-7, 1, 5, 1, 4]
value = 6


comb = combinations(arr,2)

count = 0

for c in comb:
    if sum(c) == value:
        count += 1

print(count)
