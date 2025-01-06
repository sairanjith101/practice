# Implement a program to remove duplicate lines from a file.

with open('future.txt', 'r') as file:
    lines = file.readlines()

# Use a set to remove duplicates and preserve order
unique_lines = list(dict.fromkeys(lines))

with open('future.txt', 'w') as file2:
    file2.writelines(unique_lines)

print("Duplicate lines have been removed.")

