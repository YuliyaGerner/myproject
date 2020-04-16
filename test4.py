class Flower(object):
    def factory (type):
        if type == "Poppy":
            return Poppy()
        if type == "Rose":
            return Rose()
    factory = staticmethod(factory)
class Poppy(Flower):
    def die(self):
        print("Poppy dying.")
class Rose(Flower):
    def die(self):
        print("Rose dying.")

obj = Flower.factory("Poppy")
obj.die()


