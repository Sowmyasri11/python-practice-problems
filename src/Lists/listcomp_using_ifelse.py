list1=[1,2,3]
l1=[i for i in list1]
print(l1)

l1=[i * 5 if i == 3 else i for i in list1]
print(l1)