from functions import add_expense, view_expense, get_total, view_by_category, clear_expense, save_and_quit, load_expenses

expenses = load_expenses()

print("=" *35)
print("welcome to your expense tracker".upper())
print("=" * 35)
while True:
    print("=" * 35)
    print("main menu".upper())
    print("=" * 35)
    print("1. Add expense")
    print("2. View expense")
    print("3. Get Total")
    print("4. View expense by category")
    print("5. Clear Expenses")
    print("6. Save and Quit")

    try:
        choice = int(input("Pick an option from the menu[1-6]: "))
    except ValueError:
        print("Invalid option! Try again!!")
        continue

    if choice == 1:
        add_expense(expenses)
    elif choice == 2:
        view_expense(expenses)
    elif choice == 3:
        total = get_total(expenses)
        if len(expenses) > 0:
            print(f"The total is ${total}")
    elif choice == 4:
        view_by_category(expenses)
    elif choice == 5:
        clear_expense(expenses)
    elif choice == 6:
        save_and_quit(expenses)
        break
    else:
        print("Incorrect choice... Pick an option from[1-6]!")                    
        