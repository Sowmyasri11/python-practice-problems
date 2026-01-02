import re
txt="The rain in Spain"

x=re.findall("[a-m]",txt)
print(x)


txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\\d", txt)
print(x)


txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


