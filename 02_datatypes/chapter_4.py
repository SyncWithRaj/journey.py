is_boiling = True # or 1 and False or 0
stri_count = 5
total_actions = stri_count + is_boiling # Upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False
# water_hot = True
# tea_added = True

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")