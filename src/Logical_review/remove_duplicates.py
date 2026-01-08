def find_duplicates(lst):
    org_set=set()
    duplicates_set=set()
    for i in lst:
        if i in org_set:
            duplicates_set.add(i)
        else:
            org_set.add(i)
    return list(duplicates_set)

lst=[1,2,3,4,2,4,5,6,2,1,3]
print(find_duplicates(lst))

