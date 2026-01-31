# Implementing a students tracker program.
# Import modules
import pandas as pd

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
    return True

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
    topStudents = [student for student in students[student]["Scores"] == highestScore]
    print(f"Top student in {subject} is {topStudents} with {highestScore}")

# Main function
def main():
    print("\n Students Performance Tracker")
    students = []

    while True:
        print("Choose an option")
        print("1. Add a students record")
        print("2. Print all students record")
        print("3. Compute average score")
        print("4. Filter students by 'name' or by 'subject'")
        print("5. Get the highest student")
        print("q. quit")

        print("\n\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\n Enter records")
            print("c. Change subject, students and marks")
            print("n. Add students and marks")
            print("r. return")
            choiceRecord = input("Enter what you want to do: ")
            subject = input("Enter subject: ")
            if choiceRecord == "n":
                name = input("Enter students name: ")
                score = input("Enter score: ")
                addRecord(students, name, subject, score)
            if choiceRecord == "c":
                subject = input("Enter a new subject")
                while True:
                    name = input("Enter students name: ")
                    score = input("Enter score: ")
main()