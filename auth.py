import random


database = {}
balance = 20000

def init():

    isValidOptionSelected = False
    print('Welcome to HP bank')
    
    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us if yes enter 1\nif no enter 2 \n"))
        
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print('Invalid option')

def login():
    print('******Login******')
    userEmail = input('Enter your email address\n')
    userPassword = input('Enter your password\n')
    print('You have successfully logged in')
    bankOperation()

def register():
    print('*****REGISTER*****')
    email = input('Enter your email\n')
    first_name = input('Enter your first name \n')
    last_name = input('Enter your last name \n')
    password = input('Enter your password *It should be only alphabets*\n')
    accountNumber =generateAccountNumber()

    database[accountNumber] = [email,first_name,last_name,password]
    # return database
    print('Your account number has been created')
    print('****************')
    print('Your account number is %d' %accountNumber)
    print('******************')
    print('make sure you keep it safe')


def depositFunds():
    amountDeposit = int(input('Enter a deposit amount\n'))
    print('you just deposited %d'% amountDeposit)
    print(balance+amountDeposit)

def withdrawFunds():
    withdrawAmount = int(input('Enter an amount to  withdraw\n'))
    print('you just withdrew %d'% withdrawAmount)
    print(balance-withdrawAmount)

def bankOperation():
    chooseBankOperation = int(input('Enter 1 to deposit\nEnter 2 to withdraw\nEnter 3 to check balance\n'))
    if(chooseBankOperation == 1):
        depositFunds()
    elif(chooseBankOperation == 2):
        withdrawFunds()
    elif(chooseBankOperation == 3):
        print(balance)
    else:
        print('invalid input')


def moveOn():
        continueAction=int(input('Do you want to perform another operation\nif yes enter 1\nif no enter 2\n'))
        if(continueAction == 1):
            bankOperation()
        elif(continueAction == 2):
            logout()



def generateAccountNumber():
    print('Generating account number')
    return random.randrange(1111111111,9999999999)
    print(generateAccountNumber())

def logout():
    login()



init()
moveOn()


