#SLOT_MACHINE_PROGRAM
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    '@': 2,
    '&': 3,
    '*': 4,
    '#': 2,
    '$': 1
}

def get_slot_machine_spin(rows, cols, symbols):
    #to create a list containing all the symbols based on their values in symbol_count
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #to copy the list so that the changes we apply don't affect the original list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

#0:['$', '#', '*'] --column[0]
#1:['#', '@', '&'] --column[1]
#2:['#', '&', '@'] --column[2]
        
#    $ | # | #
#    # | @ | &
#    * | & | @

#transpose the columns list
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= ' | ')
            else:
                print(column[row], end = '')

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (range: 1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount
    


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your balance is not enough to bet this amount, current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.\nTotal bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()