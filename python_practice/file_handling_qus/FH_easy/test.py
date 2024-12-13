# Open the file in read mode
with open('newfile.txt', 'r') as file:
    # Read and print the first line
    first_line = file.readline()
    print(first_line)
