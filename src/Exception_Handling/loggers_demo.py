def sum_Even(list1):
    print("sum_even() started execution")

    sum = 0
    for i in list1:
        if i%2 == 0:
            sum = sum + i
    print("sum_even() finished execution")
    return sum
def main():
    print("main() started execution")

    list1=list(map(int, input().split()))
    print("input taken from user")
    print("calling sum_Even()")
    result = sum_Even(list1)
    print(result)

main()