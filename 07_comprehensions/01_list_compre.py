menu = [
    "Masala Chai",
    "Iced lemon tea",
    "Green Tea",
    "Iced peach Tea",
    "Ginger chai",
]

# iced_tea = [tea for tea in menu if len(tea) > 12]
iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)
