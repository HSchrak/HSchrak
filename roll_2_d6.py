from random import randint

def roll_two_dice():
    die1 = randint(1, 6)
    #print(f'first die: {die1}')
    die2 = randint(1, 6)
    #print(f'Second die: {die2}')
    return die1 + die2

def main():
    num_rolls = int(input("How many times do you want to roll the dice? "))

    for _ in range(num_rolls):
        roll = roll_two_dice()
        print(f"TOTAL: {roll}")

if __name__ == "__main__":
    main()
