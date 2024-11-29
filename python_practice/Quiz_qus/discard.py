# what will be the output?
# A. KeyError
# B. ValueError
# c. {1, 2, 3, 4}
# D. {1, 2, 3}

set1 = {1, 2, 3}
set1.discard(4)
print(set1)