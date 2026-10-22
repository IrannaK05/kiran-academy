def banking_application():
  # Opening balance fixed at 10,000[cite: 3]
  balance = 10000.0

  while True:
    print("\n--- Welcome to Kiran Bank ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
      # Check balance
      print(f"Current Balance: ₹{balance:g}")

    elif choice == "2":
      # Deposit money
      try:
        deposit_amount = float(input("Enter deposit amount: "))
        if deposit_amount > 0:
          balance += deposit_amount
          print(f"Deposit successful.")
          print(f"Updated Balance: ₹{balance:g}")
        else:
          print("Invalid amount! Deposit amount must be greater than 0.")
      except ValueError:
        print("Invalid input! Please enter a valid numerical amount.")

    elif choice == "3":
      # Withdraw money
      try:
        withdraw_amount = float(input("Enter withdrawal amount: "))
        if withdraw_amount > 0:
          if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal successful.")
            print(f"Updated Balance: ₹{balance:g}")
          else:
            print("Transaction failed: Insufficient balance.")
        else:
          print("Invalid amount! Withdrawal amount must be greater than 0.")
      except ValueError:
        print("Invalid input! Please enter a valid numerical amount.")

    elif choice == "4":
      # Exit
      print("Thank you for banking with us. Goodbye!")
      break

    else:
      print("Invalid menu choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
  banking_application()