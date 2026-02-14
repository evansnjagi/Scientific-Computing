# Implementing a bisection algorithm. (approximating square root of a number)
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='bisection.log',
    filemode='a'
)
# Bisection function
def bisection(number, iterations = 100, tolerance = 1e-8):
    # Starting the function
    if number == 0:
        root = 0
        print(f"The root of {number} is: {root}")
    elif number == 1:
        root = 1
        print(f"The root of {number} is: {root}")
    else:
        root = None
        low = min(2, number)
        high = max(2, number)

        # Loop through I number of iteration
        for _ in range(iterations):
            mid = (low + high) / 2.
            midSquare = mid ** 2

            # Check if the square is within range
            if abs(midSquare - number) < tolerance:
                root = mid
            
            elif midSquare > number:
                high = mid
            else:
                low = mid
        if root is None:
            print("The root does not exist. Failed to converge!")
        else:
            print(f"The root of {number} is: {round(root, 4)}")
    return root
        


# Main function
def main():
    logging.info("Entering main function")
    # Function inputs constrains
    print("---- Bisection Calculator -----")
    print("Enter parameters below\n")

    # Get user's number input and casting to a float
    notN = True
    while notN:
        try:
            logging.info("Getting the users number input")
            N = float(input("Number (N): "))
            try:
                if N < 0:
                    logging.info(f"Got a negative real number {N}")
                    logging.debug("Raising a value error")
                    raise ValueError("Bisection root accepts real positive numbers!")
            except Exception as err:
                print(err)
            notN = False
            logging.info("Moved outside the infinite loop")
        except ValueError:
            logging.warning(f"Got an invalid input from the user: ValueError",
                            exc_info=True)
            print("Invalid number input! Try again.")
    
    # Get users input on total iterations they want
    try:
        I = int(input("Iterations (I): "))
        logging.info(f'Got the iteration value {I}')
        if I < 50:
            print("Invalid! Iterations should be above 50!")
            print("Using default iteration value!")
            I = None
            logging.info("Using default iteration because I < 50")
        elif I > 100:
            print("Computation expensive iterations. You should use fewer than 100!")
            print("Using default iteration!")
            I = None
            logging.info("Using default iteration because I > 100")
    except ValueError:
        I = None
        logging.warning("Got an invalid user iteration (I) input. Using the default value",
                        exc_info=True)
        print("Invalid iteration input! Valid input should be an integer.")
        print("Default iteration value will be used")

    # Getting tolerance as users input
    try:
        T = float(input("Tolerance (T): "))
        if not (1e-10 <= T <= 1e-6):
            T = None
            print("Out of logspace! Using default value")
            logging.info("Logspace out of range") 
    except ValueError:
        T = None
        logging.warning("Invalid users input on tolerance",
                        exc_info=True)
        print("Invalid tolerance! It should be of type float!")
        print("Using default torelance value!")

    # Envoking the bisection function
    if I is None and T is None:
        bisection(number = N, iterations = 100, tolerance = 1e-8)
    elif I is None:
        bisection(number = N, tolerance = T)
    elif T is None:
        bisection(number = N, iterations = I)
    else:
        bisection(number = N, iterations = I, tolerance = T)
# Envoking the main function
main()