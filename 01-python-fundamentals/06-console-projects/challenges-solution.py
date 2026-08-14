def main():
    balance = 1000.0  # Initial account balance

    while True:
        print("\n--- ATM Menu ---")
        print("1 - Check Balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            print(f"Current Balance: ${balance:.2f}")

        elif choice == '2':
            try:
                amount_str = input("Enter deposit amount: ").strip()
                amount = float(amount_str)
                if amount <= 0:
                    print("Error: Deposit amount must be positive.")
                else:
                    balance += amount
                    print(f"Successfully deposited ${amount:.2f}. New Balance: ${balance:.2f}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")

        elif choice == '3':
            try:
                amount_str = input("Enter withdrawal amount: ").strip()
                amount = float(amount_str)
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive.")
                elif amount > balance:
                    print(f"Error: Insufficient balance. Current balance is ${balance:.2f}.")
                else:
                    balance -= amount
                    print(f"Successfully withdrew ${amount:.2f}. New Balance: ${balance:.2f}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Error: Invalid option. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
