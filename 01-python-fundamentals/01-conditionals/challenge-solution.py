balance = float(input("Enter balance amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

errors = []

if withdrawal_amount <= 0:
    errors.append("Withdrawal amount must be positive.")

if withdrawal_amount > balance:
    errors.append("Withdrawal amount cannot exceed balance.")

if withdrawal_amount % 100 != 0:
    errors.append("Withdrawal amount must be in multiples of 100.")

if errors:
    for error in errors:
        print(error)
else:
    balance -= withdrawal_amount
    print(f"Withdrawal successful. New balance: {balance:.2f}")