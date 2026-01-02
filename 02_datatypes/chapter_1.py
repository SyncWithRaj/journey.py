
# ________________Mutability_________________
# Memory kaam kaise karti hai (mutability ke context me):

# Jab koi mutable object hota hai (jaise list),
# 👉 memory ka same address rehta hai, bas andar ka data change ho jata hai.
# Matlab: naya space nahi banta, wahi jagah update hoti hai.

# Jab koi immutable object hota hai (jaise string),
# 👉 change karne pe nayi memory ban jaati hai.
# Purani memory waise hi rehti hai, usko touch bhi nahi karta.
# ____________________________________________________________

sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 23
print(f"Second Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")