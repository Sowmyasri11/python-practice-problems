num=int(input("Enter the number:"))
temp=num
sum_cubes=0

while temp > 0 :
    digit=temp%10
    sum_cubes += digit ** 3
    temp=temp//10

if sum_cubes == num:
    print("Yes, is an amstrong number")
else:
    print("No, is not an amstrong number")

