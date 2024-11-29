text = 'Gavs Technologies'

char,index = input("Enter a char and Index value : ").split()
index = int(index)

text = text[:index] + char + text[index+1:]

print(text)