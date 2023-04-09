import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 3,
    "B": 6,
    "C": 9,
    "D": 12,
}

symbolValue = {
    "A": 25,
    "B": 12,
    "C": 6,
    "D": 4,
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines= []
    for line in range(lines):
        symbol = columns[0][line]
        for col in range(1, COLS):
            symbolToCheck = columns[col][line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
            
    return winnings, winningLines

def getSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            allSymbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for col in range(len(columns)):
            if col != len(columns) - 1:
                print(columns[col][row], end=" | ")
            else:
                print(columns[col][row], end="")
                
        print()
 
def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be bigger than 0.")
        else:
            print("please enter a number.")

    return amount

def getAmountOfLines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number.")

    return lines

def getBet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("please enter a number.")

    return amount

def spin(balance):
    lines = getAmountOfLines()
    while True:
        bet = getBet()
        totalBet = int(bet) * lines

        if totalBet > balance:
            print(f"Your bet is higher than your balance, your current balance is ${balance}")
        else:
            break

    print(f"You are currently betting ${bet} on {lines} lines. Your Total is: ${totalBet}.")


    slots = getSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)
    winnings, winningLines  = checkWinnings(slots, lines, bet, symbolValue)
    print(f"You won {winnings}!!")
    print(f"You won on lines:", *winningLines)
    return winnings - totalBet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You finished with ${balance}")
    
    
       
main()