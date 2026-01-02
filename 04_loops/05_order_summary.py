names = ["Hitesh", "Meera", "sam", "Ali"]
bills = [50, 70, 85, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")