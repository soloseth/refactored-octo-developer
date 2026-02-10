from datetime import datetime


#Account Logic

class Account:
    def __init__(self, account_number, name, pin):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = 0.0
        self.transactions = []
        self.is_active = True

    def verify_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self._record_transaction("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record_transaction("WITHDRAW", amount)

    def _record_transaction(self, txn_type, amount):
        self.transactions.append({
            "type": txn_type,
            "amount": amount,
            "balance": self.balance,
            "time": datetime.now()
        })

    def print_statement(self):
        print(f"\n--- Statement for {self.name} ---")
        for txn in self.transactions:
            print(f"{txn['time']} | {txn['type']} | {txn['amount']} | Balance: {txn['balance']}")
        print(f"Current Balance: {self.balance}\n")

    def close_account(self):
        self.is_active = False

#Bank Logic

class Bank:
    def __init__(self):
        self.accounts = {}
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


#Transaction logic

def main():
    bank = Bank()

    while True:
        print("""
ACTION MENU:
1. Create account
2. Deposit
3. Withdraw
4. Print statement
5. Close account
6. Exit
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
                acc_no = int(input("Account number: "))
                pin = input("PIN: ")
                amount = float(input("Amount: "))
                acc = bank.get_account(acc_no)
                if acc and acc.verify_pin(pin) and acc.is_active:
                    acc.deposit(amount)
                    print("Deposit successful")
                else:
                    print("Invalid details")

            elif choice == "3":
                acc_no = int(input("Account number: "))
                pin = input("PIN: ")
                amount = float(input("Amount: "))
                acc = bank.get_account(acc_no)
                if acc and acc.verify_pin(pin) and acc.is_active:
                    acc.withdraw(amount)
                    print("Withdrawal successful")
                else:
                    print("Invalid details")

            elif choice == "4":
                acc_no = int(input("Account number: "))
                pin = input("PIN: ")
                acc = bank.get_account(acc_no)
                if acc and acc.verify_pin(pin):
                    acc.print_statement()
                else:
                    print("Invalid details")

            elif choice == "5":
                acc_no = int(input("Account number: "))
                pin = input("PIN: ")
                if bank.close_account(acc_no, pin):
                    print("Account closed")
                else:
                    print("Invalid details")

            elif choice == "6":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
