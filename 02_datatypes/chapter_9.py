essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Essential Spices: {only_in_essential}")

print(f"Is'cloves' in essential Spices? : {'cloves' in essential_spices}")