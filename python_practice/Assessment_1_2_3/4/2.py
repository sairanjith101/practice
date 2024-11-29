import re

text = "Hello Gary Williams"

regex = r'([\w]+)\s([\w]+)\s([\w]+)'

match = re.match(regex, text)

print(match)

if match:
    first_match = match.group(2)
    second_match = match.group(3)
    print("First name : ", first_match)
    print("Second name : ", second_match)
else:
    print("No matches found")