# Arithmentic arranger function.
def arithmeticArranger(problems, showAnswers = False):
    if len(problems) > 5:
        return "More than 5 problems included!"
    # Problem formatting
    num1Format = []
    num2Format = []
    widthFormat = []
    answers = []
    for prob in problems:
        num1, sign, num2 = prob.split()
        width = max(len(num1), len(num2)) + 2
        # Formatting the first line(with numbers in first position)
        num1Format.append(f"{num1:>{width}}")
        num2Format.append(f"{sign} {num2:{width - 1}}")
        widthFormat.append("-"*width)

        if sign == "+":
            sol = int(num1) + int(num2)
            answers.append(f"{sol:>{width}}")
        else:
            return "Error, sign not include!"

    # Arrange in arithmetic format
    arrange = (
        "    ".join(num1Format) + "\n" +
        "    ".join(num2Format) + "\n" +
        "    ".join(widthFormat)
    )
    if showAnswers:
        arrange += (
           "\n" + "    ".join(str(a) for a in answers)
        )
    return arrange

# The main function
def main():
    problems = input("Enter: ")
    print(arithmeticArranger(problems, True))

main()