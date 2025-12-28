initial_balance = int(input("Enter the initial balance: "))
n = int(input("Enter the number of iterations: "))
balance = initial_balance
for _ in range(n):
    amount = int(input())
    if amount % 100 == 0 and balance >= amount:
        print("SUCCESS")
        balance -= amount
    else:
        print("FAILED")
print(balance)
