# Implement a program that checks if a file is readable and writable.

import os

file_path = 'newfile.txt'

if os.path.exists(file_path):
    is_readable = os.access(file_path, os.R_OK)
    is_writeable = os.access(file_path, os.W_OK)

    print(f'File {file_path} Permissions: ')
    print(f'Readable: {is_readable}')
    print(f'Writable: {is_writeable}')
else:
    print(f'File {file_path} does not exists')