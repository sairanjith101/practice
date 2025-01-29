text = 'Gavs Technologies'

char = input("Enter a Char: ")
index = int(input("Enter a Index: "))

new_text = text[:index] + char + text[index+1:]

print(new_text)