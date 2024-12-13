# Open a file in read mode and print only the first line.

# option 1

with open('newfile.txt', 'r') as file1:
    for line in file1:
        print(line)
        break

# option 2 (best)

with open('newfile.txt', 'r') as file1:
    lines = file1.readline()
    print(line)