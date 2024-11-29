# A Python program to print all
# combinations of a given length
from itertools import combinations


arr = (4, 4, 5, 3)
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations((arr), 2)

# Print the obtained combinations
for i in list(comb):
	print (i)
