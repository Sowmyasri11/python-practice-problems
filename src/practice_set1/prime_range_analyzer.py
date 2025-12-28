num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))

def is_prime(n):
    if n<=1:
        return False
    i=2
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 1
    return True

count=0
for num in range(num1,num2+1):
    if is_prime(num):
        count+=1

print(count)
