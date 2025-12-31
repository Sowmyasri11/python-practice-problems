# inefficient way
'''class Citizen:
    def __init__(self,name,age,gender,state,nationality):
        self.name=name
        self.age=age
        self.gender=gender
        self.state=state
        self.nationality=nationality
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.state)
        print(self.nationality)

def main():
    sowmya=Citizen('Sowmya',21,'Female','AP','Indian')
    suji=Citizen('Suji',22,'Female','AP','Indian')
    bhavana=Citizen('Bhavana',24,'Female','Karnataka','Indian')

    sowmya.display()
    suji.display()
    bhavana.display()


if __name__=='__main__':
    main()'''

class Citizen:
    nationality='Indian'

    def __init__(self,name,age,gender,state):
        self.name=name
        self.age=age
        self.gender=gender
        self.state=state

    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.state)
        print(self.nationality)


def main():
    sowmya = Citizen('Sowmya', 21, 'Female', 'AP')
    suji = Citizen('Suji', 22, 'Female', 'AP')
    bhavana = Citizen('Bhavana', 24, 'Female', 'Karnataka')

    print(sowmya.__dict__)      #sowmya.display()
    print(suji.__dict__)        #suji.display()
    print(bhavana.__dict__)     #bhavana.display()

    print(Citizen.__dict__['nationality'])
    print(Citizen.nationality)
if __name__ == '__main__':
    main()