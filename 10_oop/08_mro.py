# MRO = Method Resolution Order (MRO)

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala  blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):  # The first thing got called
    pass

cup = D()
print(cup.label)
# print(D.__mro__)