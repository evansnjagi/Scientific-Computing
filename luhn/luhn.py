# Implementing luhns algorithm 
# Get users input
creditCardNumber = input("Enter number: ")

# Luhn algorith function
def luhn(creditNumber):
    # Step 1: Reverse the number(right to left)
    reversedNumber = creditNumber[::-1]

    # Step 2. Get the sum of odd numbers
    oddNumber = reversedNumber[::2]
    sumOdd = 0
    for odd in oddNumber:
        sumOdd += int(odd)

    # Step 3. Get the sum of even numbers
    evenNumber = reversedNumber[1::2]
    sumEven = 0
    for even in evenNumber:
        double  = int(even) * 2
        if double >= 10:
            sumEven += double // 10 + double % 10
        else:
            sumEven += double
    totalSum = sumOdd + sumEven
    return (totalSum % 10) == 0

# Main function
def main(creditCard):
    # Creating a transition table
    cardTTable = str.maketrans({"-": "", " ": ""})
    creditNumber = creditCard.translate(cardTTable)
    if luhn(creditNumber):
        print("Valid!")
    else:
        print("Invalid!")

main(creditCardNumber)