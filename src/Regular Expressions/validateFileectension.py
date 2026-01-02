import re

file="data.csv"
pattern=r".*\.(csv|txt|json)$"
print("valid " if re.fullmatch(pattern,file) else "Invalid File")
