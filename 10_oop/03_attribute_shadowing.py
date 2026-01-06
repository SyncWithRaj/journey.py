class Chai:
    temprature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temprature)

cutting.temprature = "Mild"
cutting.cup = "small"
print("After changng", cutting.temprature)
print("Cup size is", cutting.cup)
print("Direct look into the class", Chai.temprature)

del cutting.temprature
del cutting.cup
print(cutting.temprature) # Doesn't give error bcz fallback is in class so return "hot"
print(cutting.cup) # error bcz fallback is not in class

