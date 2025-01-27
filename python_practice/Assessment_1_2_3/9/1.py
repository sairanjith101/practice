user_input = input("Enter a alphanumeric value: ")

for char in user_input:
    if char.isdigit():
        user_input = user_input.replace(char, '', 1)
        break

reverse_input = user_input[::-1]
print(reverse_input)