class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def get_balance(self):
        print(f"💰 Current Balance: ₹{self.__balance}")

# Menu-based interface
def menu():
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n=== Bank Menu ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            account.get_balance()
        elif choice == '4':
            print("👋 Thank you for banking with us!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the program
menu()
