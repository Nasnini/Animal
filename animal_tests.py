import unittest
from Animal import animal

#Animal test class:
class Animal_tests(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.dog_1 = Animal('Food','Bark')
        self.cat_1 = Animal('Food','Meow')

    def TestDogSound(self):
        
        self.assertEquals(self.dog_1.sounds, 'Bark')
        print("\nDoes the dog eat test")
        #asserts the dog barks
        #Dog - meows ----should fail


    def TestDogEats(self):
        print("\nDoes the dog bark test")
        self.assertEquals(self.dog_1.eats, 'Food')
        # Does the dog eat food ----should fail
        # Does the dog eat Food ----should pass

    def TestCatSound(self):
        print("\nDoes the cat meow test")
        self.assertEquals(self.cat_1.sounds,'Meow')
        # Does the cat "bark" ----should fail
        # Does the cat "Meow" ----should pass
        

    def TestCatEats(self):
        print("\nDoes the cat eat test")
        self.assertEquals(self.cat_1.sounds,'Food')
        # Does the cat eat meat ----should fail
        # Does the cat eat Food ----should pass
        # Does the cat eat food ----should fail

if __name__ == "__main__":
    unittest = Animal_tests()