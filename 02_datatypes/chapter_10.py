# chai_order = dict(type="Masala Chai", size="Large", sugar=2)
# print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# print(f"Recipe base: {chai_recipe['base']}")
# print(f"Recipe: {chai_recipe}")
# del chai_recipe["liquid"]
# print(f"Recipe: {chai_recipe}")

# print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order Details (keys): {chai_order.keys()}")
# print(f"Order Details (Values): {chai_order.values()}")
# print(f"Order Details (items): {chai_order.items()}")

last_item = chai_order.popitem()  # remove last item and stored in variable
print(f"Removed last item: {last_item}")

extra_spices = {"cardmom": "crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)

print(f"Updated Chai recipe: {chai_recipe}")

# chai_size = chai_order["size"]
# print(f"Chai size is: {chai_size}")

customer_note = chai_order.get("note", "No Note")
print(f"Chai size is: {customer_note}")