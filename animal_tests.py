import unittest
from animal import Animal

#Animal test class:
class Animal_tests(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def TestDogSound(self):
        pass
        #asserts the dog barks
        #Dog - meows ----should fail


    def TestDogEats(self):
        pass
        # Does the dog eat food ----should fail
        # Does the dog eat Food ----should pass

    def TestCatSound(self):
        pass
        # Does the cat "bark" ----should fail
        # Does the cat "Meow" ----should pass
        


    def TestCatEats(self):
        pass
        # Does the cat eat meat ----should fail
        # Does the cat eat Food ----should pass
        # Does the cat eat food ----should fail

if __name__ == "__main__":
    animal_tests = Animal_tests()