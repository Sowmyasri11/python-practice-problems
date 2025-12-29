import logging

logging.basicConfig(filename="log.txt", level=logging.WARNING)


def validate(mobile_number):
    if len(mobile_number) == 10:
        print("Valid Mobile Number")
    else:
        logging.warning("Mobile Number validation failed ")
        print("Invalid Mobile Number")

def main():

    mobile_number = input("Enter Mobile Number: ")
    validate(mobile_number)

main()