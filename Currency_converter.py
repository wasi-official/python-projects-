# Currency Converter — Convert between any currencies using live rates
import requests

api_key = "YOUR_API_KEY_HERE"
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

while True:
    amount = input("Enter amount or quit: ")
    if amount.lower() == "quit":
        break

    from_currency = input("Enter from currency: ").upper()
    to_currency = input("Enter to currency: ").upper()

    from_rate = data.get("rates").get(from_currency)
    to_rate = data.get("rates").get(to_currency)

    if from_rate and to_rate:
        result = (float(amount) / float(from_rate)) * float(to_rate)
        print(f"Result: {round(result, 2)} {to_currency}")
    else:
        print("Invalid currency code. Try again.")