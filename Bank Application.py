class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")


def bank_application():
    print("Welcome to the Bank!")

    # Creating accounts
    account1 = BankAccount("Rushi")
    account2 = BankAccount("Komal", 1000)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            account1.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            account1.withdraw(amount)
        elif choice == '3':
            account1.check_balance()
        elif choice == '4':
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    bank_application()