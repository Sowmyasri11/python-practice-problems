#findall

import re

text="The rain in Spain"

re_expression=re.findall("ai",text)
print(re_expression)

#search function

txt = "The rain in Spain"
x = re.search("\\s", txt)

print("The first white-space character is located in position:", x.start())


#split

x=re.split("\\s+",txt)
print(x)
x=re.split("\\s+",txt,1)
print(x)

#sub

x=re.sub("\\s+","9",txt)
print(x)