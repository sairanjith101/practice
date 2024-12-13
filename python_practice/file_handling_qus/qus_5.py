# Write a program to check if a file exists.

import os

file_path = 'sample.txt'

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

