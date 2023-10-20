def print_diamond(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the diamond: ")) # Enter the number of rows for the diamond: 5
    if n % 2 == 0:
        n += 1  # Make sure n is an odd number
    print_diamond(n)