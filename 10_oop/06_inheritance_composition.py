class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChaai(BaseChai):
    def add_spices(self):
        print("Adding cardmom, ginger, cloves.")

# Creating objects vs creating classes are the two different story
class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


class FancychaiShop(ChaiShop):
    chai_cls = MasalaChaai

shop = ChaiShop()
fancy = FancychaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()