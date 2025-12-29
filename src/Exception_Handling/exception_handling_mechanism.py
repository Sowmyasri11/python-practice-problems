def fun2():
    print('fun2() started execution')

    numerator = int(input('enter a numerator: '))
    denominator = int(input('enter a denominator: '))
    result = numerator / denominator
    print(result)
    print('fun2() finished execution')

def fun1():
    print('fun1() started execution')
    try:
        fun2()
    except ZeroDivisionError:
        print('Exception handled in fun1()')
    print('fun1() finished execution')

def main():
    print('main() started execution')
    fun1()
    print('main() finished execution')

main()
