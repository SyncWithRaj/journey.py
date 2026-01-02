# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining grams of base tea is {remaining_tea}")

milk_litres = 7
serving = 4
milk_per_serving = milk_litres / serving  # / is like float while dividing
print(f"Milk per serving is {milk_per_serving }")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots   # // is like int while dividing
print(f"Whole tea bags per pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3;
# leftover_pods = total_cardamom_pods / pods_per_cup
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")