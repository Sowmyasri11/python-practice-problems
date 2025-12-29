def fun():
    print('fun() started execution')

    try:
        numerator = int(input('Enter a number: '))
        denominator = int(input('Enter a denominator: '))
        result = numerator/denominator
        print(result)
    except ZeroDivisionError as e:
        print( 'Exception handled in fun()')
        raise e
    finally:
        print('fun() ended execution')

def main():
    print('main() started execution')
    try:
        fun()
    except:
        print('Exception handled in main()')

    print('main() ended execution')

main()


