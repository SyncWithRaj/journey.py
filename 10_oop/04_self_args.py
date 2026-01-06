class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"

cup = Chaicup()
print(cup.describe())
# print(Chaicup.describe())

chai_two = Chaicup()
chai_two.size = 100
print(Chaicup.describe(chai_two))