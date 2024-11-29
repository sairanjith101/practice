# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

##################################################################

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(secList):
	
	secList[0], secList[-1] = secList[-1], secList[0]

	return secList
	
# Driver code
secList = [1, 2, 3]
print(swapList(secList))


