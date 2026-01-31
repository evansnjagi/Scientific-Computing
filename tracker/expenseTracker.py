# Expense Tracker Program

# Import modules
import sys

# Add expense function
def addExpense(expenses, amount, category):
    expenses.append({
        "amount": amount,
        "category": category
    })
    return True

# List expenses function
def listExpenses(expenses):
    for expense in expenses:
        print(f"{expense["category"]}: {expense["amount"]}")

# Show total expenses fuction
def showTotalExpenses(expenses):
    return sum(map(lambda x: x["amount"], expenses))

# Filter expenses function
def filterExpenses(expenses, category):
    filtered = map(lambda x: x['amount'], filter(lambda x: x['category'] == category, expenses))
    print(f"Category: {category} Amount: {list(filtered)[0]}")

# Main function
def main():
    expenses = [] # Empty expeses list
    while True:
        print("\nExpense Tracker Program")
        print("1. Add an expense")
        print("2. List all expense")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("q. Exit the program")

        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            if not (addExpense(expenses, amount, category)):
                print("Error!")
        elif choice == '2':
            listExpenses(expenses)
        elif choice == '3':
            total = showTotalExpenses(expenses)
            print(f"\n Total Expenses: {total}")
        elif choice == '4':
            category = input("Enter category: ")
            filterExpenses(expenses, category)
        elif choice == 'q':
            break
        else:
            print("Invalid choice!")
            continue

main()