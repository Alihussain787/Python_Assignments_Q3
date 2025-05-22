import random

def dice():

    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    sum: int = die1 + die2

    print("First die:", str(die1))
    print("Second die:", str(die2))
    print(f"Total of two dice: {sum}")

if __name__ == "__main__":
    dice()