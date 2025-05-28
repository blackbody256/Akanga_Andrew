balance = 0
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited: {amount}")
    print(f"New balance: {balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Withdrew: {amount}")
        print(f"New balance: {balance}")

def main():
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()