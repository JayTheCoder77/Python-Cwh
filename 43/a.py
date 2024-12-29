# python slot machine
import random
def spin_row():
    symbols = ['🔔','🍒','🍉','🍋','⭐️']

    results = [random.choice(symbols) for _ in range(3)]

    return results
def print_row(row):
    print("  |  ".join(row))
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐️':
            return bet * 20
    return 0
def main():
    balance = 100
    print("*******************")
    print("WELCOME TO SLOT MACHINE")
    print("symbols 🔔🍒🍉🍋⭐️")

    while balance > 0:
        print(f"Current Balance ${balance:.2f}")
        bet = input("place bet amt")

        if not bet.isdigit():
            print("invalid")
            continue

        bet = int(bet)
        if bet > balance:
            print("insufficient balance")
            continue

        if bet <= 0:
            print("invalid")
            continue

        balance -= bet
        row = spin_row()
        print("spinnin.....")
        print_row(row)
        payout = get_payout(row,bet)
        if payout > 0:
            print("you won")
            balance += payout
        else:
            print("you lost")
        play_again = input("play again (y/n)")
        if play_again.lower() != 'y':
            break
if __name__ == '__main__':
    main()
