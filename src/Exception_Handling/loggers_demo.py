import logging
def sum_Even(list1):
    logging.info("sum_even() started execution")

    sum = 0
    for i in list1:
        if i%2 == 0:
            sum = sum + i
    logging.info("sum_even() finished execution")
    return sum
def main():
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.info("main() started execution")

    list1=list(map(int, input().split()))
    logging.info("input taken from user")
    logging.info("calling sum_Even()")
    result = sum_Even(list1)
    print(result)

main()