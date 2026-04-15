import csv
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print("Expense added")

def show_expenses():
    if not expenses:
        print("No expenses found")
    else:
        print("\nExpenses:")
        for i, exp in enumerate(expenses):
            print(f"{i+1}. {exp['name']} - ₹{exp['amount']}")

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print("Total Expense:", total)

def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Amount"])
        for exp in expenses:
            writer.writerow([exp["name"], exp["amount"]])

def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "name": row["Name"],
                    "amount": float(row["Amount"])
                })
    except:
        pass

# Load previous data
load_expenses()

# Menu loop
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        save_expenses()
        print("Expenses saved. Exiting...")
        break
    else:
        print("Invalid choice")
