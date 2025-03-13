with open('newfile.txt', 'r') as file1:
    lines = file1.readlines()
    print(lines[-1].strip())