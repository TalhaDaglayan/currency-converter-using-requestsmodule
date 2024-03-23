import requests
import json

# https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{bozulacakdoviz}.json
api_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies"

exchange_curr = input("Currency you want to exchange: ")
rcvng_curr = input("To which currency: ")
amount = int(input(f"how much '{exchange_curr}' do you want to exchange?: "))

data = requests.get(api_url + '/' + exchange_curr + ".json")
data = json.loads(data.text)

curr_date = data['date']
curr = data[exchange_curr][rcvng_curr]
calculated_amount = curr * amount

print(f"The '{exchange_curr.upper()}' to '{rcvng_curr.upper()}' exchange rate on {curr_date} is: {curr}")
print(f"You exchanged {amount} '{exchange_curr.upper()}' for the value of {calculated_amount} '{rcvng_curr.upper()}'.")