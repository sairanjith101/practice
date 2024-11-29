num1 = 10
num2 = 12
num3 = 16

if (num1 > num2) & (num1 > num3):
    print("Largest number is : ", num1)
elif (num2 > num1) & (num2 > num3):
    print("Largest number is : ", num2)
else:
    print("Largest number is : ", num3)