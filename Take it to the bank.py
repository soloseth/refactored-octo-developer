print("Welcome to my bank! Don't be shy ;), Give me all your money!!")
balance = 2830
i = 1
'''Adding commas to numbers results in a tuple, not an int'''
'''Python Tuple is an immutable (unchangeable) collection of various data type elements'''

# Initial transaction loop
while True:
    print("choose your trasnaction below:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Create New Account")
    choice = float(input("Choice: "))

    if choice == 1:
        print(f'Balance: KES {balance} ')
        break

    if choice == 2:
        try:
         num = float(input("Deposit: "))
         balance +=num
         print(f'Balance: KES {balance}')
         break
        except ValueError:
         print("Error! Please give a valid amount.")

    if choice == 3:
        try:
         num = float(input("Withdraw: "))
         balance -= num
         print(f'Balance: KES {balance}')
         break
        except ValueError:
            print("Error! Please give a valid amount.")

    if choice == 4:
        print(f'Successful! Your new account number is A0000000{i}')
        i+= 1
        break


#Continuing transaction loop
while True:
    opt = input("would you like to make another transaction? Yes or no: ")
    if opt == 'no':
        print("thank you for banking with us, goodbye!")
        break
    elif opt == 'yes':
        print("choose your trasnaction below:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Create New Account")
        choice = float(input("Choice: "))

        if choice == 1:
            print(f'Account Balance: KES {balance} ')

        if choice == 2:
            try:
                num = float(input("Deposit: "))
                balance += num
                print(f'New Balance: KES {balance}')
            except ValueError:
                print("Error! Please give a valid amount.")

        if choice == 3:
            try:
                num = float(input("Withdraw: "))
                if num > balance:
                    print("Not enough money, your account balance is ",{balance})
                    break

                balance -= num
                print(f'New Balance: KES {balance}')
            except ValueError:
                print("Error! Please give a valid amount.")

        if choice == 4:
            print(f'Successful! Your new account number is A0000000{i}')
            i += 1
