class Animal:
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds

    def Food(self):


        print("{0} eats".format(self.name))

    def sound(self):

        print("{0} barks".format(self.sounds))

dog = Animal("Rax", "Dog")
cat = Animal("Storm", "Cat")

dog.food()
dog.sound()
    