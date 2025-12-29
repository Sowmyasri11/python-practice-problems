names=['John', 'James','Emmy', 'Michael', 'Jimmy']

#creating new list which contains names containing  J
'''
j_names=[]
for name in names:
    if 'J' in name:
        j_names.append(name)

print(j_names)
'''

#using list_comprehesion
j_names=[name for name in names if 'J' in name]
print(j_names)

names_copy=[name for name in names]
print(names_copy)
