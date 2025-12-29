import logging

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b
def main():
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    logging.debug(f'a= {a}')
    logging.debug(f'b= {b}')

    result1=addition(a,b)
    logging.debug(f'result1= {result1}')
    result2=subtraction(a,b)
    logging.debug(f'result2= {result2}')
    result3=multiplication(a,b)
    logging.debug(f'result3= {result3}')
    result4=division(a,b)
    logging.debug(f'result4= {result4}')

main()