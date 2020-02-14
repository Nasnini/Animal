#Import Super class from animal
from animal import Animal

class Dog(Animal):
    def __init__(self, name, sounds):
        super().__init__(name, sounds)

    def food(self):
        print(self.name + "eats")
    
    def sound(self):
        print(self.sounds + " barks")

Dog_1 = Dog("Rax", "Dog")

Dog_1.food()
Dog_1.sound()