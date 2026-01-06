class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))   #<class 'type'>  
# In python world all class are objects itself and other also some things known as objects, search about it

ginger_tea = Chai()
print(type(ginger_tea))  # <class '__main__.Chai'>
print(type(ginger_tea) is Chai) # True bcz ginger_tea object belongs to a Chai class
print(type(ginger_tea) is ChaiTime) # False bcz ginger_tea object do not belongs to a ChaiTime class but it belongs to Chai class