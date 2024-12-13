import os

file_path = 'sample.txt'

if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)

    print(f'File {file_path} size: {file_size} bytes')
else:
    print(f'File {file_path} does not exists')