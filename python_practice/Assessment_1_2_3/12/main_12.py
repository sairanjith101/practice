names = { 3 : 'Apple', 5 : 'Water Melon', 10 : 'Orange', 2 : 'Fig' }
result = []

for key in sorted(names.keys()):
    value = names[key]
    result.append(value[:key] + value[key+1:])

print(tuple(result))

# Explanation:

# 1.The input dictionary names contains the given values and their corresponding keys, which will be used as the index to remove the character.
# 2.The sorted() function is used to sort the keys in ascending order.
# 3.The for loop iterates through the sorted keys.
# 4.For each key, the corresponding value is retrieved from the names dictionary.
# 5.The character at the index position is removed by concatenating the first part of the string (before the index) with the second part of the string (after the index).
# 6.The resulting modified string is added to the output list.
# 7.Finally, the output list is converted to a tuple and printed as the desired output.
