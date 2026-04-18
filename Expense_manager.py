# Expense Manager — Add, view, and track expenses with file saving
expenses = []

def load_data(expenses):
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(":")
                expenses.append((name, int(amount)))
    except FileNotFoundError:
        print("No previous expense found")

def add_expenses(expenses):
    name = input("Enter the name: ")
    amount = int(input("Enter the amount: "))
    expenses.append((name, amount))

def view_all_expenses(expenses):
    for i, (name, amount) in enumerate(expenses, 1):
        print(f"{i}. {name}: {amount}")

def total(expenses):
    j = sum(amount for name, amount in expenses)
    print(f"Total amount = {j}")

def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for name, amount in expenses:
            file.write(f"{name}:{amount}\n")

load_data(expenses)
while True:
    print("---WELCOME---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total")
    print("4. Quit")
    i = input("ENTER: ")
    if i == "1":
        add_expenses(expenses)
    elif i == "2":
        view_all_expenses(expenses)
    elif i == "3":
        total(expenses)
    elif i == "4":
        break
    else:
        print("Invalid option")

save_expenses(expenses)