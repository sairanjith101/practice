n = int(input("Enter a value: "))

try:
    with open('sample.txt', 'r') as file1:
        for i, line in enumerate(file1):
            if i < n:
                print(line, end='')
            else:
                break
except FileNotFoundError:
    print(f'File {file1} does not fount')