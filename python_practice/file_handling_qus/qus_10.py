# Write a program to create a new file if it doesn't exist.

try:
    with open('newfile.txt', 'x') as file1:
        file1.close()
        print("File Successfully Created")
except FileExistsError:
    print("File already exists")