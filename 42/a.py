#banking program

def show_balance(balance):
    print(f"Balance is {balance:.2f} $")
def deposit():
    amount = float(input("enter amt to deposit"))
    if amount < 0:
        print("invalid amt")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("enter amt to withdraw"))
    if amount < 0:
        print("invalid amt")
        return 0
    elif amount > balance:
        print("insufficient balance")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("enter choice")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("invalid choice")

    print("Thank you")


if __name__ == '__main__':
    main()