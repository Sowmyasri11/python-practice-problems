import re

s = "abcdefghij"
if re.fullmatch(r".{10}", s):
    print("Valid length")
else:
    print("Invalid length")
