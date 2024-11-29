arr1 = (10,20,30,40,60)
arr2 = (70,80,90,100,200)

even_num_index = arr1[0::2]
print("Add number index value is : ", even_num_index)

odd_num_index = arr2[1::2]
print("Odd number index value is : ", odd_num_index)

output = even_num_index + odd_num_index
print("Both index  value is : ", output)
print("Both index value sum of : ", sum(output))