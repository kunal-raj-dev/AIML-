from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

    def hunt(self):
        print("Lion is hunting")

    def sleep(self):
        print("Lion is sleeping")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()
lion.hunt()
lion.sleep()

cow = Cow()
cow.make_sound()