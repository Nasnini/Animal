#Import from the Animal Class
from animal import Animal

class Cat(Animal):
    def __init__(self, name, sounds):
        super().__init__(name, sounds)

    def food(self):
        print(self.name + "eats")
    
    def sound(self):
        print(self.sounds + "Meow")

cat_1 = Cat("Storm", "Cat")

cat_1.food()
cat_1.sond()
