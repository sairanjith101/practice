givenlist = [-1, 1, 2, 3, 0, -2, 7, 8]
print("The given list is : ", givenlist)
newlist = list(range(givenlist[0],givenlist[-1]+1))
print("The new list is in range of  (-2 to 8)", newlist)
missingnumber = set(givenlist)^set(newlist)
print("Missing number in givenlist ", missingnumber)
