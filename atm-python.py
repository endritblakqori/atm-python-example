balance = 1000


def pin_code():
    pin_tries = 1
    while pin_tries <= 3:
        pin = input("Please enter your pin code: ")
        if len(pin) != 4:
            print("Pin code must contain 4 numbers! Please recheck your pin!")
        else:
            if pin == "1234":
                main()
            else:
                print(f"Given pin code is wrong! You have {3 - pin_tries} tries!")
                pin_tries += 1
    print("\n You have given a wrong pin code 3 times! Please contact your local Python Banking branch!")


def view_balance():
    print(f"Your balance is {balance}€")
    menu()


def withdraw_cash():
    global balance
    while True:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw > balance:
            print(f"You don't have enough money to withdraw {withdraw}€, your balance is {balance}€")
            menu()
        else:
            print("\n"f"You have withdrawn {withdraw}€, remaining balance is {balance - withdraw}€")
            balance -= withdraw
            ask = int(input("If you want to perform another operation, press 1, to exit press 0: "))
            if ask == 1:
                menu()
            else:
                exit_atm()


def deposit_cash():
    global balance
    while True:
        deposit = int(input("Enter the amount you want to deposit: "))
        if deposit <= 4:
            print("Only deposits over 5€ are accepted")
        else:
            balance += deposit
            print(f"You have deposited {deposit}€, your new balance is {balance}€")
            ask = int(input("If you want to perform another operation, press 1, to exit press 0: "))
            if ask == 1:
                menu()
            else:
                exit_atm()


def exit_atm():
    print("\n""Thank you for using Python Banking ATM. Have a nice day!")
    exit()


def menu():
    print("   1. View balance", "\n"
          "   2. Withdraw money", "\n"
          "   3. Deposit money", "\n"
          "   4. Exit")
    while True:
        option = int(input("Choose one of the options above (Write number 1-4): "))
        if option < 1 or option > 4:
            print("Please only write number from 1 to 4")
        elif option == 1:
            view_balance()
        elif option == 2:
            withdraw_cash()
        elif option == 3:
            deposit_cash()
        elif option == 4:
            exit_atm()


def main():
    print("*** Welcome to Python Banking ***")
    menu()


pin_code()
