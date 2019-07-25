#Passenger Card

class PassCard:

    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        self.__value = 0
    
    def addCash(self, new):
        if new > 0:
            self.__value += new
            return 'Value added!'
        else:
            return 'Invalid!'
    
    def showCash(self):
        return 'Your cash: R$%.2f' %self.__value
    
    def payPass(self, value):
        if value > 0:
            if self.__value > 0:
                self.__value -= value
            else:
                return 'Insufficient Credits'
        else:
            return 'Invalid!'

class Student(PassCard):

    def __init__(self, number, name, inst):
        PassCard.__init__(self, number, name)
        self.__inst = inst
    
    def payStudent(self, cash):
        return self.payPass(cash/2)

class Worker(PassCard):
    def __init__(self, number, name, company):
        PassCard.__init__(self, number, name)
        self.__Company = company
    
    def payWorker(self, cash):
        return self.payPass(cash)

def Main():

    while True:
        print('Welcome!\n1-Student\n2-Worker\n3-Exit')
        op = input('Answer: ')
        if op == '1':
            number = input('Number: ')
            name = input('Name: ')
            inst = input('Your school or your college: ')
            Stud = Student(number, name, inst)
            print('Add cash? Y/N')
            answer = input('Answer: ').upper()
            if answer == 'Y':
                Cash = input('Add Credit: ')
                try:
                    Cash = int(Cash)
                    print(Stud.addCash(Cash))
                    print()
                    print(Stud.showCash())
                    print()
                except:
                    print('Invalid!')
            
            elif answer == 'N':
                print('Thank you.')
            
            else:
                print('Invalid Access!')
                Main()
            
            print('Do you want to pay your pass? Y/N')
            pay = input('Answer: ').upper()
            if pay == 'Y':
                ValuePass = 3.45
                print(Stud.payStudent(ValuePass))
                print(Stud.showCash())
            
            elif pay == 'N':
                print('Thanks!')
            
            else:
                print('Invalid Access!')
            
        elif op == '2':
            number = input('Number: ')
            name = input('Name: ')
            comp = input('Your Company: ')
            Work = Worker(number, name, comp)
            print('Add cash? Y/N')
            answer = input('Answer: ').upper()
            if answer == 'Y':
                Cash = input('Add Credit: ')
                try:
                    Cash = int(Cash)
                    print(Work.addCash(Cash))
                    print()
                    print(Work.showCash())
                    print()
                except:
                    print('Invalid!')
            
            elif answer == 'N':
                print('Thank you.')
            
            else:
                print('Invalid Access!')
                Main()
            
            print('Do you want to pay your pass? Y/N')
            pay = input('Answer: ').upper()
            if pay == 'Y':
                ValuePass = 3.45
                print(Work.payWorker(ValuePass))
                print(Work.showCash())
            
            elif pay == 'N':
                print('Thanks!')
            
            else:
                print('Invalid Access!')
        
        elif op == '3':
            print('Turn off!')
            break

Main()




    


