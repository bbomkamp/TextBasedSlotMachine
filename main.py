#Current Progress: 38:28
#Youtube Video Addy: https://www.youtube.com/watch?v=th4OBktqK1I&ab_channel=TechWithTim

import random

#CONSTANTS(Final).
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#Specify the amouth of rows and cols in slot machine.
ROWS = 3
COLS = 3

#Symbols.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #"items()" give you the key and value of a dictionary.
    #Loop through dictionary(symbol_count).
    #symbol/Key symbol_count/Value.
    for symbol, symbol_count in symbols.items():
        #You can use "_"(Anonymous Variable) in place of a variable like "i" is your not going to use it in iteration. Its called an "Unused Variable".
        #Add symbol(Key) to the dictionary symbol_count(Value) amount of times.
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []

    for _ in range(cols):
        column = []

        #Copy all_symbols list.
        #The "[:]" is known as a "Slice Operator".
        #Using a Slice Operator ensures we copy a list instead of refrencing the original.
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            #Remove symbol option from current_symbols.
            #Finds first instance within the list and removes it.
            #This is done so it doesn't get picked again.
            current_symbols.remove(value)
            #Add random value to the column
            column.append(value)

        columns.append(column)    
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        #Loops thourgh all of the items in "columns" parameter.
        #Prints first row, then 2nd, then etc....
        for i, column in enumerate(columns):
            #Stuctures the board using th index.
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")   
        #Brings print down to the next line. Becuase it prints a new line charecter by default and the end of teh empty Print Statment.         
        print()

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
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")

    #Think of each slot as a column.
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()