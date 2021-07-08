users = {}

def line():
    print("="*50)

def home():
    print()
    line()
    print("\t WELCOME TO DELTA BANK")
    line()
    input(" Press ENTER to continue ")
    print()
    login()


def login():
    print(" Login as :")    
    print("\t 1. Admin")
    print("\t 2. User")
    print("\t 3. Back to Home Page")
    print()
    selection = input(" Select login option: 1 or 2 or 3: ")
    print(selection)

    if(selection == "1"):
        adminLogin()

    elif(selection == "2"):
        userLogin()

    elif(selection == "3"):
        home()

    else:
        print(" Invalid Entry. Please enter a valid choice")
        login()


def adminLogin():
    adminPass = 1234
    inputPass = int(input(" Please enter Admin Password: "))

    if (adminPass == inputPass):
        print(" Login Successful")
        adminMenu()
    else:
        home()


def adminMenu():
    print()
    line()
    print("\t Welcome to the Admin console")
    line()
    print(" Please select yout preferred service")
    print("\t 1. Add User")
    print("\t 2. Delete User")
    print("\t 3. List users")
    print("\t 4. Back to Home Page")
    print("\t 5. Add automatic user")
    print()
    choice = input(" Select Service: (1 or 2 or 3 or 4 or 5): ")

    if choice == "1":
        addUserDetails()
        adminMenu()

    elif choice == "2":
        deleteUserDetails()
        adminMenu()

    
    elif choice == "3":
        getUsers()
        adminMenu()

    elif choice == "4":
        home()

    elif choice == "5":
        addUser("1", "Kevin", "1245")
        adminMenu()  

    else:
        print("Invalid Entry")
        adminMenu()       


def addUserDetails():
    acc_Number = input(" Please enter account number: ")
    acc_Name = input(" Enter name: ")
    pin_No = input(" Enter the pin number: ")
    addUser(acc_Number, acc_Name, pin_No)


def addUser(accountNo, name, pin):
    users[accountNo] = {'userName': name, 'pin':pin, "balance":{"KES": 0, "USD": 0}}
    print(" Account number {} for {} added successfully".format(accountNo, name))


def getUsers():
    print(users)
    return users


def deleteUserDetails():
    acc = input(" Please enter the account number to delete: ")

    if (acc in users.keys()):
        users.pop(acc)
        print(" DELETION SUCCESSFUL: Account Number {} Deleted".format(acc))
        adminMenu()

    else:
        print(" Account not Saved. Please enter a valid account")
        adminMenu()


def userLogin():
    accountTries = 0
    while (accountTries < 3):
        accNo = input(" Please enter your account number: ")
        accountTries += 1

        if(accNo in users.keys()):
            pinTries = 0

            while(pinTries < 3):
                userPin = input(" Please enter your pin: ")
                pinTries += 1

                if(userPin == users[accNo]["pin"]):
                    line()
                    print(" Login Successful")
                    userMenu(accNo)

                else:
                    print(" You entered the wrong pin. You have {} tries left".format(3-pinTries))
                    print()

            print(" MAXIMUM TRIES REACHED. PLEASE TRY AGAIN LATER!!!!")
            print()
            login()
        
        else:
            print(" Invalid Account. Please enter a valid account number")

    home()

def userMenu(acc):
    print()
    account = acc
    user = users[acc]["userName"]
    print()
    line()
    print("\t Hello {}, Welcome to your User Menu".format(user))
    line()
    print(" Please select yout preferred service")
    print("\t 1. Withdraw Funds")
    print("\t 2. Deposit Funds")
    print("\t 3. Check Balance")
    print("\t 4. Change Pin")
    print("\t 5. Exit to home")
    
    choice = input(" Select Service: (1 or 2 or 3 or 4 or 5): ")

    if choice == "1":
        withdrawFunds(account)

    elif choice == "2":
        depositFunds(account)

    elif choice == "3":
        checkBalance(account)

    elif choice == "4":
        changePin(account)

    elif choice == "5":
        home()
    
    else:
        print(" Invalid Entry")
        userMenu(account) 


def getKESBalance(acc):
    KESbalance = users[acc]["balance"]["KES"]
    return KESbalance

def getUSDBalance(acc):
    USDbalance = users[acc]["balance"]["USD"]
    return USDbalance


def getBalance(acc, currency):
    if (currency == "KES"):
        KESbalance = users[acc]["balance"]["KES"]
        return KESbalance

    if (currency == "USD"):
        USDbalance = users[acc]["balance"]["USD"]
        return USDbalance

    else:
        print(" Invalid Currency")


def withdrawFunds(acc):
    account = acc
    print(" Please select currency to withdraw in:")
    print("\t 1. KES")
    print("\t 2. USD")
    currency = input(" Please select your preferred currency (1 or 2): ")

    if (currency == "1"):
        withdraw = "KES"
        balance = getBalance(account, withdraw)

    elif (currency == "2"):
        withdraw = "USD"
        balance = getBalance(account, withdraw)

    else:
        print(" Invalid Entry")
        userMenu(account)

    withdrawAmt = int(input(" How much do you wish to withdraw?: "))
            
    if (balance > withdrawAmt):
        confirm = input(" Please confirm withdrawal of KES {} : (Y or N)".format(withdrawAmt))
        confirm = confirm.upper()
            
        if (confirm == "Y"):
            newBalance = balance - withdrawAmt
            users[account]["balance"][withdraw] = newBalance
            print(" Withdrawal Successful. New balance is {} {}".format(withdraw, newBalance))
            print()
            printReceipt = input(" Do you want a receipt? (Y or N): ")
            printReceipt = printReceipt.upper()

            if (printReceipt == "Y"):
                print("\t Initial Balance: {} {}".format(withdraw, balance))
                print("\t Withdrawal Amount: {} {}".format(withdraw, withdrawAmt))
                print("\t Current Balance: {} {}".format(withdraw, newBalance))
                userMenu(account)

            else:
                userMenu(account)

    else:
        print(" Insufficient Funds")
        print(" Current balance is {} {}".format(withdraw, balance))
        userMenu(account)


def depositFunds(acc):
    account = acc
    print(" Please select currency to deposit in:")
    print("\t 1. KES")
    print("\t 2. USD")
    currency = input(" Please select your preferred currency (1 or 2): ")

    if (currency == "1"):
        deposit = "KES"
        balance = getBalance(account, deposit)

    elif (currency == "2"):
        deposit = "USD"
        balance = getBalance(account, deposit)

    else:
        print(" Invalid Entry. Please use Y or N")
        userMenu(account)

    depositAmt = int(input(" How much do you wish to deposit?: "))
    
    confirm = input(" Please confirm deposit of {} {} : (Y or N) ".format(deposit, depositAmt))
    confirm = confirm.upper()
        
    if (confirm == "Y"):
        newBalance = balance + depositAmt
        users[account]["balance"][deposit] = newBalance
        print(" Deposit Successful. New balance is {} {}".format(deposit, newBalance))
        print()
        printReceipt = input("Do you want a receipt? (Y or N): ")
        printReceipt = printReceipt.upper()

        if (printReceipt == "Y"):
            print("\t Initial Balance: {} {}".format(deposit, balance))
            print("\t Deposit Amount: {} {}".format(deposit, depositAmt))
            print("\t Current Balance: {} {}".format(deposit, newBalance))
            userMenu(account)

        else:
            userMenu(account)

    else:
        userMenu(account)


def checkBalance(acc):
    account = acc
    usd = getUSDBalance(account)
    kes = getKESBalance(account)
    print(" Your account balance is : ")
    print("\t KES {}".format(kes))
    print("\t USD {}".format(usd))    
    userMenu(account)


def changePin(acc):
    currentPin = users[acc]["pin"]
    pin = input(" Please eneter your current pin: ")

    if (pin == currentPin):
        newPin = input(" Please enter your new pin: ")
        newPin2 = input(" Please re-enter your new pin: ")

        changeAttempts = 0
        
        while (changeAttempts < 3):
            if(newPin == newPin2):
                users[acc]["pin"] = newPin
                print(" Pin changed successfully")
                userMenu(acc)

            else:
                changeAttempts += 1
                print(" The pins did not match. Please try again")
                print( " You have {} attempts left".format(3-changeAttempts))
                print()
                changePin(acc)

        print(" You have reached the maximum pin change attempts. Please try again later")
        userMenu(acc)

    else:
        print(' You have entered the wrong pin. Please try again')
        userMenu(acc)
