# Each objects has it's own entity that's called as namespace (it can possess its own features, it's own properties but doesn't bother other ones)

class Chai:
    origin = "India"  # Inside the class whenever the variable goes then it's called as properties

print(Chai.origin)

Chai.is_hot= True  # Now this is also the property of class Chai
print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False;

# print(f"Class: {Chai.is_hot}")
print("Class:", Chai.is_hot) #Upper-line and this line has different chatGPT it when u get confused

print(f"Masala: {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)
print(masala.flavor)
