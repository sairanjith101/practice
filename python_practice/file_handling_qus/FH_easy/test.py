num_of_lines = 0

with open('newfile.txt', 'r') as file1:
    lines = file1.readlines()
    for line in lines:
        num_of_lines += 1

print(num_of_lines)