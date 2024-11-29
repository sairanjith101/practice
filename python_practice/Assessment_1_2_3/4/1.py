import re

text = "Hello Gary Williams"

regex = r'([\w]+)\s([\w]+)\s([\w]+)'

match = re.search(regex, text)

if match:
    print("First match : ", match.group(2))
    print("Second match : ",match.group(3))
else:
    print("match not found")