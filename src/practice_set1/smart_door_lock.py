correct_pin = input("ENTER THE PIN: ")
access = False

for i in range(3):
    attempt = input()
    if attempt == correct_pin:
        access = True
        break

if access:
    print("ACCESS GRANTED")
else:
    print("LOCKED")
