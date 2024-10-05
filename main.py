import time
import os

def help():
    print('Ver == 5.2.4-3.12.7')
    print('Thank you for using virenv.')
    print('#==================================')
    time.sleep(1)
    print('All callable func :')
    print('virenv.help()')
    print('virenv.virenv.convertTypeSI(<argument>)')
    print('virenv.virenv.converttype(<argument>)')
    print('virenv.virenv.factorial(<argument>)')
    print('virenv.virenv.testmain()')
    print('virenv.virmenu.greet(<type>)')
    print('virenv.virmenu.start_program1()')
    print('#==================================')
    time.sleep(1)
    print('to set up(standard) :')
    print('use `from virenv import virenv`')
    print('#==================================')

class Parent:
    def __init__(self, txt):
        self.message = txt  

    def printmessage(self):
        print(self.message)

    def convertTypeSI(self, val):
        val = int(val)
        return val
    
    def converttype(self, argu):
        ctype = input('type(shortened) : ')
        if ctype == 'str':
            argu = str(argu)
            time.sleep(0.2)
            return argu
        elif ctype == 'int':
            argu = int(argu)
            time.sleep(0.2)
            return argu
        elif ctype == 'bool':
            argu = bool(argu)
            time.sleep(0.2)
            return argu
        elif ctype == 'float':
            argu = float(argu)
            time.sleep(0.2)
            return argu
        elif ctype == 'complex':
            argu = complex(argu)
            time.sleep(0.2)
            return argu
        else:
            print('There is no type of ' + str(ctype) + '. Try another type.')
            time.sleep(0.5)
            return argu
         
    def factorial(self, n):
        if n == 0 or n ==1:
            return 1
        else:
            return n * self.factorial(n - 1)
        
    def testmain(self):
        if __name__ == '__main__':
            print('This is the main program')
        else:
            print('This program is being imported as a module')
    
    def greet(self, type):
        name = input('customers name : ')
        resn = input('name : ')
        if type == 'welcome':
            print('Hello ' + name + '. Welcome to ' + resn + '!')
        else:
            print('no data logged in for type <' + type + '>')

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

virenv = Child("Hello, and welcome!")

class Parent2:
    def __init__(self, txt2):
        self.message = txt2  

    def greet(self, type):
        name = input('customers name : ')
        resn = input('name : ')
        if type == 'welcome':
            print('Hello ' + name + '. Welcome to ' + resn + '!')
        elif type == 'goodbye':
            print('~~sayonara~~')
        elif type == 'view menu':
            self.display_menu()
        else:
            print('no data logged in for type <' + type + '>')
    
    def display_menu(self):
        print('please select the following option : ')
        print('1) Add Expense')
        print('2) View Expense')
        print('3) View Summary')
        print('vlog) View all log')
        print('q) Exit Program')

    def promt_expense(self):
        description = input('Enter your description : ')
        amount = float(input('Enter your expense amount : '))
        if amount < 0:
            print('amount must more than 0!')
            return None
        category = input('Enter your expense catagory : ')
        with open('expense.csv', 'at') as file:
            row = f'{description},{amount},{category}\n'
            file.write(row)
        print(description, amount, category)

    def log(self, logrow):
        with open('log.log', 'at') as file:
            logrow = str(logrow)
            file.write(logrow)

    def view_expense(self):
        with open('expense.csv', 'rt', encoding='UTF-8') as file:
            expense = file.read()
            print(expense)

    def view_log(self):
        with open('log.log', 'rt', encoding='UTF-8') as file:
            log = file.read()
            print(log)

    def view_summary(self):
        with open('expense.csv', 'rt', encoding='UTF-8') as file:
            expenses = file.readlines()
            expenses_stat = {}
            sum_expense = {}
            for expense in expenses:
                expense_split = expense.split(',')
                expense_name = expense_split[0]
                expense_amount = float(expense_split[1])
                expense_category = expense_split[2].strip()

                if not expenses_stat.get(expense_category):
                    expenses_stat[expense_category] = {}

                if not expenses_stat[expense_category].get(expense_name):
                    expenses_stat[expense_category][expense_name] = 0

                expenses_stat[expense_category][expense_name] += expense_amount

            print(expenses_stat)

        for k, v in expenses_stat.items():
            sum_expense[k] = 0
            for v2 in v.values():
                sum_expense[k] += v2
                

        total_expense = sum(sum_expense.values())
        
        print(sum_expense.items())

        print('\n' + f'total is {total_expense} bath\n')

    def del_log(self):
        with open('log.log', 'wt') as file:
            ...
        time.sleep(0.1)
        self.log('cleared `log.log` at ' + str(time.localtime()) + '\n')

    def del_expense(self):
        with open('expense.csv', 'wt') as file:
            ...
        time.sleep(0.1)
        self.log('cleared `expense.csv` at ' + str(time.localtime()) + '\n')

    def start_program1(self):
        while True:
            self.display_menu()
            try:
                user_option = input('Enter your option : ')
                user_option = int(user_option)
            except ValueError:
                user_option = user_option
            if user_option == 1:
                self.log('users_option == 1 at ' + str(time.localtime()) + '\n')
                self.promt_expense()
            elif user_option == 2:
                self.log('users_option == 2 at ' + str(time.localtime() + '\n'))
                self.view_expense()
            elif user_option == 3:
                self.log('users_option == 3 at ' + str(time.localtime()) + '\n')
                self.view_summary()
                time.sleep(2)
            elif user_option == 'vlog':
                self.log('users_option == vlog at ' + str(time.localtime()) + '\n')
                self.view_log()
            elif user_option == 'q':
                self.log('users_option == `q` | exit at ' + str(time.localtime()) + '\n')
                print('~~sayonara~~')
                break
            else:
                self.log('users_option == Key Error | exit at ' + str(time.localtime()) + '\n')
                print('Key Error : thats not in option')
                break


class Child2(Parent2):
    def __init__(self, txt2):
        super().__init__(txt2)

virmenu = Child2('Hello, and Welcome!')