from datetime import datetime

# Account logic

class Account ():
    def __init__ (self, account_number, name, pin):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = 0.0
        self.transactions = [] #list
        self.is_active = True

    def verify_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Not a valid amount for deposit")
        self.balance += amount
        self.record_transaction( "DEPOSIT", amount)

    def transfer_in(self, amount):
        if amount <= 0:
            raise ValueError("Not a valid amount for transfer")
        self.balance += amount
        self.record_transaction( "RECEIVED", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Not a valid amount for withdrawal")
        if amount > self.balance:
            raise ValueError("Insufficient funds! You ain't got no money!")
        self.balance -= amount
        self.record_transaction("DEPOSIT", amount)

    def transfer_out(self, amount):
        if amount <= 0:
            raise ValueError("Not a valid amount for transfer")
        if amount > self.balance:
            raise ValueError("Insufficient funds! You ain't got no money!")
        self.balance -= amount
        self.record_transaction( "SENT", amount)


    def record_transaction(self, txn_type, amount):
        self.transactions.append({
            "Type": txn_type,
            "Amount": amount,
            "Balance": self.balance,
            "Time": datetime.now()
        })

    def print_statement(self):
        print(f"\n--- Statement for {self.name} Account No. {self.account_number}---")
        for txn in self.transactions:
            print(f"{txn['Time']} | {txn['Type']} | {txn['Amount']} | Balance: {txn['Balance']}")
        print(f"Current Balance: {self.balance}\n")

    def close_account(self):
        self._record_transaction("CLOSED ACCOUNT:")
        self.is_active = false


#BANK LOGIC

class Bank:
    def __init__(self):
        self.accounts = {} #Directory
        self.next_account_number = 1001

    def create_account(self, name, pin):
        acc = Account(self.next_account_number, name, pin)
        self.accounts[self.next_account_number] = acc
        self.next_account_number += 1
        return acc.account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def close_account(self, account_number, pin):
        acc = self.get_account(account_number)
        if acc and acc.verify_pin(pin):
            acc.close_account()
            return True
        return False


#TRANSACTION LOGIC

def main():
    bank = Bank()

    while True:
        print("""
    ACTION MENU:
    1. Create account
    2. Deposit
    3. Withdraw
    4. Transfer to Another Account
    5. Print statement
    6. Close account
    7. Exit
    """)

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Name: ")
                while True:
                    pin = input("Set PIN: ")
                    pin2 = input("Confirm PIN: ")
                    if pin == pin2:
                        break
                    else:
                        print("Could not confirm PIN. Please try again")

                acc_no = bank.create_account(name, pin)
                print(f"Account created. Account Number: {acc_no}")

            elif choice == "2":
                acc = bank.get_account(int(input("Account number: ")))
                pin = input("PIN: ")
                amount = float(input("Amount: "))
                if acc and acc.verify_pin(pin) and acc.is_active:
                    acc.deposit(amount)
                    print("Deposit successful")
                else:
                    print("Invalid details")

            elif choice == "3":
                acc = bank.get_account(int(input("Account number: ")))
                pin = input("PIN: ")
                amount = float(input("Amount: "))
                if acc and acc.verify_pin(pin) and acc.is_active:
                    acc.withdraw(amount)
                    print("Withdrawal successful")
                else:
                    print("Invalid details")

            elif choice == "4":
                acc1 = bank.get_account(int(input("Your Account Number: ")))
                acc2 = bank.get_account(int(input("Receiving account number: ")))
                pin = input("PIN: ")
                amount = float(input("Amount: "))
                if acc1 and acc1.verify_pin(pin) and acc1.is_active and acc2 and acc2.is_active:
                    acc1.transfer_out(amount)
                    acc2.transfer_in(amount)
                    print("Transfer successful")
                else:
                    print("Invalid Details")

            elif choice == "5":
                acc = bank.get_account(int(input("Account number: ")))
                pin = input("PIN: ")
                if acc and acc.verify_pin(pin):
                    acc.print_statement()
                else:
                    print("Invalid details")

            elif choice == "6":
                acc = int(input("Account number: "))
                pin = input("PIN: ")
                if bank.close_account(acc, pin):
                    print("Account closed")
                else:
                    print("Invalid details")

            elif choice == "7":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()





