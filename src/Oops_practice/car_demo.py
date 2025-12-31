class Car:
    def __init__(self):
        self.brand='BMW'
        self.cc=2100
        self.color='red'
    def start_engine(self):
        print("Engine is starting")

    def shift_gear(self):
        print("Shifting gear")

    def accelerate(self):
        print("car is accelerating")

def main():
    c1=Car()
    print(c1.brand)
    print(c1.cc)
    print(c1.color)
    c1.start_engine()
    c1.shift_gear()
    c1.accelerate()

    c2=Car()
    print(c2.brand)
    print(c2.cc)
    print(c2.color)
    c2.start_engine()
    c2.shift_gear()
    c2.accelerate()
if __name__=='__main__':       # this method gets executed only when file is executed in script mode
    main()



