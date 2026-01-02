import re
#s="12345sowmya"
s="12345"
if re.fullmatch(r"\d+",s):
    print("Only digits")
else:
    print("Not only digits")