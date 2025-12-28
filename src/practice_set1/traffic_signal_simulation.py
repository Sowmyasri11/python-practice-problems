T = int(input("Enter the time: "))


time = T % 90

if time == 0:
    time = 90

if 1 <= time <= 30:
    print("RED")
elif 31 <= time <= 45:
    print("YELLOW")
else:
    print("GREEN")
