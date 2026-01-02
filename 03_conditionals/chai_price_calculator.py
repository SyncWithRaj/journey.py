cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is Rs.10")
elif cup == "medium":
    print("Price is Rs.15")
elif cup == "large":
    print("Price is Rs.20")
else:
    print("Unknown cup size")