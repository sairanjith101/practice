import itertools

arr = (4, 4, 5, 3)
target_sum = 8

#arr = (-7, 1, 5, 1, 4)
#target_sum = 6

combinations = itertools.combinations(arr, 2)  # all combinations of length 3
count = 0

for comb in combinations:
    if sum(comb) == target_sum:
        count += 1
    print(comb)

print("Number of combinations with sum", target_sum, "is", count)
