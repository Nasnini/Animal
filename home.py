#Import Super class from Animal
from animal import Animal
from cat import Cat
from dog import Dog

class Home():
    def __init__(self, pets=[]):
        self.pets = pets

    def adopt_Pet(self, pet):
        for each in self.pets:
            if each == pet:
                raise Exception("Cannot adopt more than one animal.")
        self.pets.append(pet)

if __name__ == "__main__":
    home = Home()
    dog1 = Dog("Rax","Barks")
    cat1 = Cat("Storm", "Meow")

    home.adopt_Pet(dog1)
    home.adopt_Pet(cat1)
    print(home.pets[0].name)