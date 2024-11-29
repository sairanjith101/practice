text = 'Gavs Technologies'

# Get the character and index from the user
char, index = input("Enter a character and an index separated by a space: ").split()
index = int(index)

# Replace the character in the text
text = text[:index] + char + text[index+1:]

# Print the updated text
print(text)
