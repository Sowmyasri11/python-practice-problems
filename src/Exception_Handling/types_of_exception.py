print('Execution started manually')
list=[10,20,30,40,50]
dict={1:'C', 2:'Java', 3:'Python', 4:'C++'}

try:
    rank = int(input('Enter the rank of the language: \n'))
    print(dict[rank])

    numerator = int(input('Enter the index of numerator: \n'))
    denominator = int(input('Enter the index of denominator: \n'))
    print(list[numerator] / list[denominator])
except:
    print('Hey there was an issue ! ')


print('Execution terminated normally')

