

# Retrieves User Deposit.
def deposit():

    #Loops til a number is returned.
    while True:
        amount = input("How much would you like to deposit to your total? $")
        #Check if input is postive number.
        if amount.isdigit():
            #Convert the inputted String to an Int.
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that 0.")
        else:
            print("Please enter a number.")

    return amount

def main():
    balance = deposit()    

main()