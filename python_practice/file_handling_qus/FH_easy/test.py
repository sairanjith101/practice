with open('check.txt', 'r') as file:
    lines = file.readlines()
    if lines:
        print(lines[-1].strip())
    else:
        print("file does not exists")