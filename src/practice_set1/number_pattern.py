number = input("Enter a number: ")
is_increasing = True

for i in range(len(number) - 1):
    if number[i] >= number[i + 1]:
        is_increasing = False
        break

if is_increasing:
    print("YES")
else:
    print("NO")
