distance=int(input("Enter the distance in meters: "))

age=int(input("Enter the age in years: "))

fare=distance*2

if age >= 60:
    fare=fare - (fare * 0.30)
elif age < 12:
    fare=fare- (fare*0.50)

print(int(fare))
