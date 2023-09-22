
amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount_due = amount_due - coin
    else:
        continue
# it's posiible that the 'amount_due' become a negetive num; so we use abs() to make it posetive.
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")