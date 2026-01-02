import re

email = "abc12@gmail.com"
pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
