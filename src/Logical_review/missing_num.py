lst = [1, 2, 3, 5, 6, 7]
n = len(lst) + 1
listsum = sum(lst)
orgSum = n * (n + 1) // 2

missing_element = orgSum - listsum
print(missing_element)
