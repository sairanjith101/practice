from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "WoW"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animal = Animal()
dog = Dog()
cat = Cat()

print(f'Dog Make Sound: ', {dog.make_sound()})
print(f'Cat Make Sound: ', {cat.make_sound()})
