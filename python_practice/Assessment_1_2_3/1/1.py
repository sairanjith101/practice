arr = [-5, 0, 2, 10]
arr.sort()
print("Given array is : ", arr)
new_arr = list(range(arr[0],arr[-1]+1))
print("New Array is : ", new_arr)
missing_number = set(arr)^set(new_arr)
print("Missing numbers is  : ", missing_number)
poss = [mn for mn in missing_number if mn>=0]
print("Positive missing number is : ", poss)
print("Smallest missing positive number : ", min(poss))
