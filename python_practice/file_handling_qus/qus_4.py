# Create a file and write multiple lines of text to it.

lines = [
    "Good Morning To All \n",
    "I am RK \n",
    "I am from Trichy \n",
    "I am a Python Developer \n"
]

with open('sample3.txt', 'w') as file1:
    line = file1.writelines(lines)