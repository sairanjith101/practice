# Create the dictionary with the given values:
names = { 3: 'Apple', 5: 'Water Melon', 10: 'Orange', 2: 'Fig' }
# Create an empty list to store the modified names:
modified_names = []
# Loop through the keys in the dictionary and remove the character at that index using string slicing.
# Append the modified name to the modified_names list:
for key in names:
    modified_names.append(names[key][:key-1] + names[key][key:])
# Print the modified names:
print(tuple(modified_names))
