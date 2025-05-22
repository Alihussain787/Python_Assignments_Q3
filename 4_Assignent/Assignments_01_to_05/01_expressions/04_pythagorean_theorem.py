import math

print("Pythagorean theorem")

def main():

    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    bc = math.sqrt(ab**2 + ac**2)

    print(f"Length of BC (hypotenuse) is {bc:.2f}")

if __name__ == "__main__":
    main()