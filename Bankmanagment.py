class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, account_holder)
            self.accounts[account_number] = new_account
            print(f"Account created successfully for {account_holder}.")
        else:
            print("Account number already exists. Please choose a different account number.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")

    def __str__(self):
        return "\n".join([str(account) for account in self.accounts.values()])


def main():
    bank = Bank()

    while True:
        print("---------------------------------------------")
        print("Welcome to the Bank Management System")
        print("---------------------------------------------")
        print("\nBanking Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")


        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            bank.create_account(account_number, account_holder)

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Balance for account {account_number}: ${account.get_balance()}")

        elif choice == '5':
            print("Thank you for using the Banking Management System.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()




