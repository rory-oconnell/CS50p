amount = 50

while amount > 0:
    print("Amount Due: ", amount)
    prompt = input("Insert Coin: ")
    if int(prompt) == 5 or int(prompt) == 10 or int(prompt) == 25:
        prompt = prompt.strip()
        amount = int(amount) - int(prompt)

print("Change Owed:", abs(amount))