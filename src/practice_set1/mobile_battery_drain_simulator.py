drain = int(input("Enter the drain amount"))

battery = 100
minutes = 0

while battery > 0:
    battery = battery - drain
    minutes = minutes + 1

print(minutes)
