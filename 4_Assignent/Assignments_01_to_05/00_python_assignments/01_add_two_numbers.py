def add():
    print("Add two numbers")
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    total = num1 + num2
    print(f"Total sum of {num1} and {num2} is {total}")

if __name__ == '__main__':
    add()