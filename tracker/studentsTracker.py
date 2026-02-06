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
# Print function
def printFace():
    print("\nChoose an option")
    print("\t1. Add a students record")
    print("\t2. Print all students record")
    print("\t3. Compute average score")
    print("\t4. Filter students by 'name' or by 'subject'")
    print("\t5. Get the highest student")
    print("\tq. quit")
    print("\n")
    choice = input("Enter your choice: ")
    return choice
    
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
    if not students:
        print("No students records are recorded!")
    else:
        data = pd.DataFrame(students)
        print("\n------------students performance data------------")
        print(data.to_string(index=False))

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

# Choice one function 
def choiceOne(students):
    logging.debug("Adding a students record section")
    print("\n-----< You are on Enter Students Record Section >-----")
    print("\ts. Add subject and marks")
    print("\tn. Add students and marks")
    print("\tr. return")

    userChoice = input("\nEnter your choice: ")
    if userChoice == "s":
        studentsName = input("Enter students name: ")
        student = True
        while student:
            # Get the subject
            subject = input("Enter Subject: ")

            # get the marks
            try:
                score = int(input(f"Enter {studentsName}, {subject} scores: "))
                addRecord(students, studentsName, subject, score)

                # Getting user input if they want to continue or return 
                userConcent = input("continue (c) or return (r): ")

                if userConcent == "c":
                    continue
                elif userConcent == "r":
                    student = False
                else:
                    print("Enter a valid escape character (c or r)")
                    continue

            except Exception as err:
                print("Invalid score! Try again.")
                logging.error(f"Invalid score type inputed {err}")
                continue
    elif userChoice == "n":
        subjectName = input("Enter subject: ")
        subject = True
        while subject:
            studentName = input("Enter students name: ")
            try:
                score = int(input(f"Enter {studentName}, {subjectName} scores: "))
                addRecord(students, studentName, subjectName, score)

                userConcent = input("continue (c) or return (r): ")

                if userConcent == "c":
                    continue
                elif userConcent == "r":
                    subject = False
                else:
                    print("Enter a valid escape character (c or r)")
                    continue
            except Exception as err:
                print("Invalid score! Try again.")
                logging.error(f"Invalid score input with the error {err}.")
                continue      
    elif userChoice == "r":
        return True
    else:
        print("Invalid input character! Try again.")    

# Fuction to hundle choice three section.


# Main function
def main():
    logging.debug("Started the main program")
    print("\nStudents Performance Tracker")
    students = []

    # Envoking the UI function
    while True:
        choice = printFace()
        if choice == "1":
            choiceOne(students)
        # Print record
        elif choice == "2":
            printRecord(students)
        # Quiting
        elif choice == "q":
            print("Goodbye!")
            break
        

main()