import re

txt="apple,banana;grape|orange"
items=re.split(r"[,;|]",txt)
print(items)