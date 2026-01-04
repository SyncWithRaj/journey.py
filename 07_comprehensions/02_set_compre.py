favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)


recipes = {
    "Masala Chai": ["giner", "cardmom", "clove"],
    "Elaichi Chai": ["cardmom", "milk"],
    "Spicy Chai": ["giner", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)