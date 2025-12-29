print('Execution started manually')
list=[10,20,30,40,50]
dict={1:'C', 2:'Java', 3:'Python', 4:'C++'}

try:
    rank = int(input('Enter the rank of the language: \n'))
    print(dict[rank])

    numerator = int(input('Enter the index of numerator: \n'))
    denominator = int(input('Enter the index of denominator: \n'))
    print(list[numerator] / list[denominator])
except KeyError:
    print('key does not exist')
except ZeroDivisionError:
    print('cannot divide by zero')
except IndexError:
    print('index out of range')
except Exception as e:
    print(e)     # uses dunder str method to display the  exception message

print('Execution terminated normally')

