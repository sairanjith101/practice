from itertools import combinations

arr = (4, 4, 5, 3)
given_sum = 8

comb = combinations(arr, 2)
count = 0

for i in list(comb): 
    if sum(i) == given_sum: 
        count += 1
  
print("Number of combination with given sum is:", count)