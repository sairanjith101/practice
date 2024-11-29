givenlist = (-1, 1, 2, 3, 0, -2, 7, 8)
#givenlist = (10, 20, 1, 2)
#givenlist = (-5, 0, 2, 10)

print("The given tuple is : ", givenlist)
sample = list(givenlist)
sample.sort()
print("Tuple covert into list is : ", sample)
newlist = list(range(sample[0],sample[-1]+1))
print("The new list is in range of : ", newlist)
missingnumber = set(givenlist)^set(newlist)
print("Missing number in givenlist : ", missingnumber)
miss = [m for m in missingnumber if m >= 0]
print("Missing smallest positive number is : ", min(miss))
