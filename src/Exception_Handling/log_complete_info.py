import logging

logging.basicConfig(filename="log.txt", level=logging.ERROR, filemode="w",\
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def fun():
    list1 = [10.20, 30, 40, 50]
    dict = {1:'C', 2:'Java', 3:'python', 4:'C++'}

    try:
        rank = int(input("Enter the rank of the language: "))
        print(dict[rank])

        numerator = int(input("Enter the index of numerator: "))
        denominator = int(input("Enter the index of denominator: "))
        result = (list1[numerator] / list1[denominator])
        print(result)
    except KeyError :
        print("key does not exist")
    except IndexError :
        print("Index out of bounds")
    except ZeroDivisionError:
        print("division by zero")

    except :
        print("Hey, some issue occurred")
        logging.error('Exception occurred', exc_info=True)

def main():
    fun()

main()
