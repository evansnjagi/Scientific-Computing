# Implementing a bisection algorithm. (approximating square root of a number)

# Bisection function
def bisection(number, iterations = 100, tolerelance = 1e-8):
    pass

# Main function
def main():
    # Function inputs constrains
    print("---- Bisection Calculator -----")
    print("Enter parameters below\n")

    # Get user's number input and casting to a float
    notN = True
    while notN:
        try:
            N = float(input("Number (N): "))
            try:
                if N < 0:
                    raise ValueError("Bisection root accepts real positive numbers!")
            except Exception as err:
                print(err)
            notN = False
        except ValueError:
            print("Invalid number input! Try again.")


# Envoking the main function
main()