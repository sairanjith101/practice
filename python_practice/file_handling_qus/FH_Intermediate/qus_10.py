n = int(input("Enter the number of lines to read: "))

try:
    with open('sample.txt', 'r') as file1:
        for i, line in enumerate(file1):
            if i < n:
                print(line, end='')
            else:
                break
except FileNotFoundError:
    print("File does not exists")