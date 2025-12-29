import logging

logging.basicConfig(filename= "log.txt",  level=logging.ERROR, filemode="w")
def div():
    try:
        numerator = int(input("Enter a numerator: "))
        denominator = int(input("Enter a denominator: "))
        quotient = numerator / denominator
        print(quotient)
    except:
        logging.error("Invalid input",exc_info=True)
def main():
    div()
main()