number = int(input("Enter a number : "))

res_num = 0

while number > 0:
    reminder = number % 10
    res_num = res_num*10 + reminder
    number //= 10

print(f'Reversed number : {res_num}')

################################################

number = input("Enter a number : ")
num = number[::-1]
print(num)