# Implementing a students tracker program.
# Import modules
import pandas as pd
import logging

# Instantiating logging
logging.basicConfig(
    filename = "studentsTracker.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

# Add a students recored fuction
def addRecord(students, name, subject, score):
    """Students is an empty list"""
    students.append(
        {
            "Name": name,
            "Subject": subject,
            "Score": score
        }
    )
    logging.debug(f"Added the {name} {subject} score as: {score}")

# Print students record function
def printRecord(students):
    data = pd.DataFrame(students)
    print("\n .........Students Record Data.............")
    print(data)

# Compute averange score
def averageScore(students, filterType):
    # Filtering
    filtered = filter(lambda student: student[filterType], students)

    # Mapping each filtered item to an average score
    averageScore = sum(map(
        lambda student: students["score"],
        filtered
    ))

    # Printing the results
    print(f"\n Average score: {averageScore}")

# Find the highest scoring student
def highestScoring(students, subject):
    # Creating a list of all scores
    totalScores = students["scores"]
    highestScore = 0
    for i in range(len(totalScores)):
        if highestScore < totalScores[i]:
            highestScores = totalScores[i]
    topStudents = [student for student in students[students]["Scores"] == highestScore]
    print(f"Top student in {subject} is {topStudents} with {highestScore}")

# Main function
def main():
    logging.debug("Started the main program")
    print("\nStudents Performance Tracker")
    students = []

    while True:
        print("\nChoose an option")
        print("\t1. Add a students record")
        print("\t2. Print all students record")
        print("\t3. Compute average score")
        print("\t4. Filter students by 'name' or by 'subject'")
        print("\t5. Get the highest student")
        print("\tq. quit")
        print("\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            logging.debug("Adding a students record section")
            print("\tEnter records")
            print("\tc. Change subject and marks")
            print("\tn. Add students and marks")
            print("\tr. return")

            # Getting users input on their choice record and the subject to recotd
            choiceRecord = input("Enter what you want to do: ")
            subject = input("Enter subject: ")

            changeRecord = True
            while changeRecord:
                if choiceRecord == "n":
                    name = input("Enter students name: ")

                    # Validate scores
                    try:
                        score = int(input("Enter students scores: "))
                        addRecord(students, name, subject, score)
                        logging.info("added students record successfully")

                        # Continue or go back to something else
                        escapeKey = True
                        while escapeKey:
                            backContinue = input("go back (r) or continue (c): ")
                            if backContinue == "c":
                                escapeKey = False
                                continue

                            elif backContinue == "r":
                                changeRecord = False
                                escapeKey = False

                            else:
                                print("Enter a valid escape key!")
                                logging.debug("Handle wrong escape key by repromting the user")
                                continue
                    except Exception as err:
                        logging.debug("Handled exception error gracefuly")
                        print(f"Invalid score type: {err}")
                        print("Try again! Score was never recorded")
                        continue
                

main()