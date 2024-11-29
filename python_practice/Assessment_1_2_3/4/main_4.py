import re

text = "Hello Gary Williams"

# Define regex pattern
#pattern = r'^Hello\s(\w+)\s(\w+)$'
regex = r'([\w]+)\s([\w]+)\s([\w]+)'

# Match regex pattern against text
match = re.match(regex, text)

print(match)

if match:
  # Get the first and last name from the regex match object
  first_name = match.group(2)
  last_name = match.group(3)

  # Print first and last name
  print("First Name:", first_name)
  print("Last Name:", last_name)
else:
  print("No match found")
