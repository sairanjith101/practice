User_input = 'abc123def'
print("The user input of alphanumeric value is : ", User_input)

for char in User_input:
    if char.isdigit():
        output = User_input.replace(char, '', 1)
        break

str_rev = output[::-1]
print("The reverse alphanumeric is : ", str_rev)