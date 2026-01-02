# ingredients = ["water", "milk", "black tea"]
# ingredients.append("sugar")
# print(f"Ingredients are: {ingredients}")
# ingredients.remove("water")
# print(f"Ingredients are: {ingredients}")

# spice_option = ["ginger", "cardamom"]
# chai_ingredients = ["water", "milk"]

# chai_ingredients.extend(spice_option)
# print(f"Chai: {chai_ingredients}")

# chai_ingredients.insert(2, "black tea")  # Insert black tea at 2nd place

# print(f"Chai: {chai_ingredients}")

# last_added = chai_ingredients.pop()
# print(f"{last_added}")
# print(f"Chai: {chai_ingredients}")
# chai_ingredients.reverse()
# print(f"Chai: {chai_ingredients}")
# chai_ingredients.sort()
# print(f"Chai: {chai_ingredients}")

# sugar_level = [1, 2, 3 ,4, 5]
# print(f"Maximum sugar level: {max(sugar_level)}")
# print(f"Minimum sugar level: {min(sugar_level)}")



# base_liquid = ["water", "milk"]
# extra_flavour = ["ginger"]
# 
# full_liquid_mix = base_liquid + extra_flavour
# print(f"Liquid mix: {full_liquid_mix}")
# 
# strong_brew = ["black_tea"] * 3
# strong_brew = ["black_tea", "water"] * 3
# print(f" Strong Brew: {strong_brew}")



raw_spice_data = bytearray(b"CINNAMON")
# raw_spice_data.replace(b"CINNA", b"CARD")   #Use below one see docs if needed
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")

