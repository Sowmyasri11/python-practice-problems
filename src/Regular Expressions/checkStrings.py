import re

s = "Hello World"
if re.match(r"Hello", s):
    print("Starts with Hello")
else:
    print("Do not start with Hello")
