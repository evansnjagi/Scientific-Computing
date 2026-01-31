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