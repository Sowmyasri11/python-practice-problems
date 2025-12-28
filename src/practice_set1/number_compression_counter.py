number = int(input("Enter the number: "))
count = 0

while number % 2 == 0:
    number = number // 2
    count = count + 1

print(count)
