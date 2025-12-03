is_valid = True
balance = 50000
correct_pin = 123

if is_valid:
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("1. Withdraw\n2. Check Balance\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful. Remaining balance:", balance)
            else:
                print("Insufficient balance.")
        elif choice == 2:
            print("Current balance:", balance)
        elif choice == 3:
            print("Thank you for visiting")
        else:
            print("Invalid option selected")
    else:
        print("Wrong PIN")
else:
    print("Card is invalid")
