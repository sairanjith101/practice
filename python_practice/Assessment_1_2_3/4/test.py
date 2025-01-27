import re

text = "Hello Gary Williams"

regex = r'([\w]+)\s([\w]+)\s([\w]+)'

match = re.finditer(regex, text)

for m in match:
    print(m.group(2))
    print(m.group(3))
