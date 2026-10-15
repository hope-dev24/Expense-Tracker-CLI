def add_expense(expenses):
    expense_name = input("Enter expense name: ")
    if expense_name.strip() == "":
        print("name cannot be empty!!")
        return

    categories = ["Food", "Bills", "Entertainment", "Transport", "Other"]
    print(f"The available categories are; {categories}")
    category = input("choose from the provided categories! ")
    if category.strip().capitalize() not in categories:
        print(f"invalid input! pick a category from {categories}")
        return

    try:
        expense_amount = float(input("Enter the amount spent on expense: "))
        if expense_amount <= 0:
            print("Amount must be greater than Zero")
            return
    except ValueError:
        print("Invalid input! Please enter a valid amount!!")
        return
    expense = {"name": expense_name, "amount": expense_amount, "category": category.strip().capitalize()}
    expenses.append(expense)
    print("=" * 25)
    print("Expense Added!!")
    print(f"Name: {expense['name']}")
    print(f"Amount: ${expense['amount']}")
    print(f"Category: {expense['category']}")
    print("=" * 25)

def view_expense(expenses):
    if len(expenses) == 0:
        print("Expenses list is empty... Start by adding one!!")
        return
    else:
        print("=" * 25)
        print("your expenses".upper())
        print("=" * 25)
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}.")
            print(f"Name - {expense['name']}")
            print(f"Amount - ${expense['amount']}")
            print(f"Category - {expense['category']}")
            print("-" * 25)

def get_total(expenses):
    if len(expenses) == 0:
        print("List is empty!!")
        return 0
    else:
        total = 0
        for expense in expenses:
            total += expense['amount']
        return total

def clear_expense(expenses):
    if len(expenses) == 0:
        print("Expenses list is empty!!")
        return
    else:
        confirm = input("Are you sure you want to clear all expenses?! ")
        if confirm.strip().lower() in ["yes", "y"]:
            expenses.clear()
            print("Expenses Cleared!")
        else:
            print("CANCELLED!!")        

def view_by_category(expenses):
    if len(expenses) == 0:
        print("Can't perform this because the list is empty!!")
        return
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else:
            category_totals[category] = expense['amount']
    print("=" * 25)
    print("spending by category".upper())
    print("=" * 25)
    for category, total in category_totals.items():
        print(f"{category}: ${total}")
    print("=" * 25)

def save_and_quit(expenses):
    if len(expenses) == 0:
        print("List is empty!")
        return
    else:
        try:
            with open("expenses.txt", "w") as file:
                for expense in expenses:
                    file.write(f"{expense['name']} | ${expense['amount']} | {expense['category']}\n") 
            print("Expenses saved! Goodbyee!!")        
        except Exception as e:
            print(f"something went wrong at {e}")
            return

def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(" | ")
                    name = parts[0].strip()
                    amount = float(parts[1].strip().replace("$", ""))
                    category = parts[2].strip().capitalize() if len(parts) > 2 else "Other"
                    expense = {"name": name, "amount": amount, "category": category}
                    expenses.append(expense)
    except FileNotFoundError:
        print("No Saved Expenses Found!!")
    return expenses                

                      

    


            


