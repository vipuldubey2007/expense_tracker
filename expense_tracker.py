
class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

expense1 = Expense(200, "food", "lunch")
expense2 = Expense(1400, "movie", "Date")
expense3 = Expense(160, "coffee", "snack")

expenses = [
    expense1,
    expense2,
    expense3
]

for expense in expenses:
    print(expense.amount)
    print(expense.category)
    print(expense.description)


while True:
    print("============EXPENSE TRACKER==========")
    print("Add Expenses")
    print("View Expenses")
    print("Calculate Total")
    print("Search Expenses")
    print("Save Expenses")
    print("EXIT")

    choice = input("Enter your choice Spydaa: ")

    if choice == "1":
        # Add Expenses
        pass

    elif choice == "2":
        # View Expenses
        pass

    elif choice == "3":
        # Calculate Total
        pass

    elif choice == "4":
        # Search Expenses
        pass

    elif choice == "5":
        # Save Expenses
        pass

    elif choice == "6":
        print("Goodbye Sir!!")
        break

    else:
        print("Invalid choice. DumbAss. Try again")


        

