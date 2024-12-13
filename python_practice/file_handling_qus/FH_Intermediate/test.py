n = int(input("Enter the number of lines to read: "))

try:
    with open('sample.txt', 'r') as file:
        for i, line in enumerate(file):
            if i < n:
                print(line, end='')
            else:
                break
except FileNotFoundError:
    print('Flie does not exists')