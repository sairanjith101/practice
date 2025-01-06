user = 'The quick Brow Fox'

upper_letter = 0
lower_letter = 0

# Remove spaces from the string
new_user = user.replace(" ", "")

# Iterate through the characters in the string
for i in new_user:
    if i.isupper():  # Check if the character is uppercase
        upper_letter += 1
    elif i.islower():  # Check if the character is lowercase
        lower_letter += 1

# Print the results
print("Uppercase letters:", upper_letter)
print("Lowercase letters:", lower_letter)
