
def deposit():
    while True:
        amount = input("How much would you like to deposit to your total? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that 0.")
        else:
            print("Please enter a number.")

    return amount

deposit()    

