n = int(input("Enter a value: "))

with open('newfile.txt', 'r') as file:
    lines = file.readlines()
    for i,value in enumerate(lines):
        if i < n:
            print(value, end='')