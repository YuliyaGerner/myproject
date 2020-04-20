import random


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"
class Cow:
    def speak(self):
        return "moo"

    def __str__(self):
        return "Cow"

class CatFactory:
    def get_animal(self):
        return Cat()

    def get_food(self):
        return "cat food"

class CowFactory:
    def get_animal(self):
        return Cow()

    def get_food(self):
        return "cow food"

class Farm:

    def __init__(self, animal_factory = None):
        self.animal_factory = animal_factory
    def show_animal(self):
        animal = self.animal_factory.get_animal()
        animal_food = self.animal_factory.get_food()
        print("this is a lovely", animal)
        print("it says", animal.speak())
        print("it eats", self.animal_factory.get_food())

def get_factory():
    return random.choice([CatFactory, CowFactory])()


shop = Farm()
for i in range(2):
    shop.animal_factory = get_factory()
    shop.show_animal()
    print("=" * 10)






