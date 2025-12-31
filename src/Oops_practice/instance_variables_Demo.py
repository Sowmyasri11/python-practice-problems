class FootBaller:
    def __init__(self,name,team,goals):
        self.name = name
        self.team = team
        self.goals = goals

    def shooting(self):
        print(self.name," is shooting")

    def passing(self):
        print(self.name," is passing")

    def running(self):
        print(self.name," is running")

    def display(self):
        print(self.name)
        print(self.team)
        print(self.goals)

def main():
    cr=FootBaller('Critiana','Juventus',745)
    cr.display()

    cr.shooting()
    cr.passing()
    cr.running()

    messi=FootBaller('Messi','Barcelona',700)
    messi.display()
    messi.shooting()
    messi.passing()
    messi.running()

if __name__ == '__main__':
    main()
