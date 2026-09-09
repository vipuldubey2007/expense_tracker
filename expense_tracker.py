class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

def add_expense():
    amount = float(input("Enter the amount:  "))
    category = input("category = ")
    description = input("description = ")

    new_expense = Expense(amount, category, description)
    expenses.append(new_expense)


def view_expenses():

    if expenses == []:
        print("No Expense found!")
    else:
        for expense in expenses:
            print(f"{expense.amount} | {expense.category} | {expense.description}")


def calculate_total():
    total = 0
    for expense in expenses:
        total = total + expense.amount
    print(total)


def search_expenses():
    search_term = input("Enter item name: ").lower()
    for expense in expenses:
        if search_term in expense.category.lower() or search_term in expense.description.lower():
            print(f"{expense.amount} | {expense.category} | {expense.description}")





expense1 = Expense(200, "food", "lunch")
expense2 = Expense(1400, "movie", "Date")
expense3 = Expense(160, "coffee", "snack")

expenses = [
    expense1,
    expense2,
    expense3
]
   


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
        add_expense()
        

    elif choice == "2":
        # View Expenses
        view_expenses()

    elif choice == "3":
        # Calculate Total
        calculate_total()

    elif choice == "4":
        # Search Expenses
        search_expenses()

    elif choice == "5":
        # Save Expenses
        pass

    elif choice == "6":
        print("Goodbye Sir!!")
        break

    else:
        print("Invalid choice. DumbAss. Try again")
#done with step 9. now move to STEP 10
