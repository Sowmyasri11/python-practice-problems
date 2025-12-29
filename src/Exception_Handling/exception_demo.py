print('Secure connection has been established to bank server')

try:
    principal_amount = int(input("Enter  principal amount : "))
    time_duration = int(input("Enter  the duration : "))
    rate_of_interest = 10

except:
    print("provide numerical value")
else:
    simple_interest = (principal_amount * time_duration * rate_of_interest) / 100
    print('simple_interest = ', simple_interest)

print("connection has been close to the server")




