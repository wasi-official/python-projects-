# Finance Tracker — Track income/expenses in any currency, converted to PKR
import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

def new_transfer(data):
    trans_type = input("Send or Receive: ").lower()
    reason = input("Enter transfer name: ")
    amount = float(input("Enter amount: "))

    if trans_type == "receive":
        type_i = "add"
    elif trans_type == "send":
        type_i = "subtract"
    else:
        print("Invalid. Type 'send' or 'receive'")
        return None

    currency = input("Enter currency type: ").upper()
    currency_rate = data.get("rates").get(currency)
    pkr = data.get("rates").get("PKR")

    if currency_rate:
        converted = round((amount / float(currency_rate)) * float(pkr), 2)
        return type_i, reason, converted
    else:
        print("Invalid currency code.")
        return None

def load_transactions(transaction):
    try:
        with open("transaction.txt", "r") as file:
            for line in file:
                trans_type, reason, amount = line.strip().split(":")
                transaction.append((trans_type, reason, amount))
    except FileNotFoundError:
        print("No old data found")

def total_funds(transaction):
    total = 0
    for trans_type, reason, amount in transaction:
        if trans_type == "add":
            total += float(amount)
        elif trans_type == "subtract":
            total -= float(amount)
    print(f"Total balance: {round(total, 2)} PKR")

def view_transactions(transaction):
    for i, (trans_type, reason, amount) in enumerate(transaction, 1):
        print(f"{i}. {trans_type} | {reason} | {amount} PKR")

transaction = []
load_transactions(transaction)

while True:
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Total balance")
    print("4. Quit")
    n = input("---: ")

    if n == "1":
        result = new_transfer(data)
        if result:
            trans_type, reason, amount = result
            transaction.append((trans_type, reason, amount))
    elif n == "2":
        view_transactions(transaction)
    elif n == "3":
        total_funds(transaction)
    elif n == "4":
        break

with open("transaction.txt", "w") as file:
    for trans_type, reason, amount in transaction:
        file.write(f"{trans_type}:{reason}:{amount}\n")