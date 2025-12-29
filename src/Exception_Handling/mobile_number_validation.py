class InvalidMobileNumberError(Exception):
    pass

def validate(mobile_number):
    if len(mobile_number) == 10:
        print('Valid mobile number')
    else:
        raise InvalidMobileNumberError("Enter a proper 10 digit mobile number")

def main():
    mobile_number=input("Enter a mobile number")
    validate(mobile_number)

main()