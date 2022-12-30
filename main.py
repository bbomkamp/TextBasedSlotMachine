#CONSTANTS(Final)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def get_number_of_lines():

    #Loops til a number is returned.
    while True:
        lines = input("How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")

        #Check if input is postive number.
        if lines.isdigit():

            #Convert the inputted String to an Int.
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter and number between 1 - " + str(MAX_LINES))
        else:
            print("Please enter a number.")

    return lines    

def get_bet():

    #Loops til a number is returned.
    while True:
        amount = input("How much would you like to bet on each line? $")

        #Check if input is postive number.
        if amount.isdigit():

            #Convert the inputted String to an Int.
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()

    print(balance, lines)    

main()