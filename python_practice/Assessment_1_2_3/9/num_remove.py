User_Input = "abc123def"

cha_str = "" .join((z for z in User_Input if not z.isdigit()))
print(cha_str)