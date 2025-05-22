print("Dicesimulator")
import random

def roll_dice():

    dial_1 = random.randint(1, 6)
    dial_2 = random.randint(1, 6)

    sum = dial_1 + dial_2

    print(f"Total of two dice: {sum}")

def main():
    dial_1 = 10
    print(f"dial1 in main() starts as: {dial_1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"dial1 in main() is: {dial_1}")

if __name__ == "__main__":
    main()