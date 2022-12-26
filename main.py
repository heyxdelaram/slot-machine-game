#SLOT_MACHINE_PROGRAM

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5


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
                print("Amount must be between ${MIN_BET} and ${MAX_BET}.")
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


main()