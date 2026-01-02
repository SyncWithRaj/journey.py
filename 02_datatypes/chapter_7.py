masala_spices = ("cardamon", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio  # Swap
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")

# Membership
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")  # Case sensitive