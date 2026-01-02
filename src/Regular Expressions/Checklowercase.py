import re
s="python"
if re.fullmatch(r"[a-z]+",s):
    print("only lower case")
else:
    print("Invalid string")