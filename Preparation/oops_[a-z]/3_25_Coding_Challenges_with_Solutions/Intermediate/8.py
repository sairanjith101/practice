# 🐾 Animal Sound System Using Polymorphism

class Animal:
    def make_sound(self):
        print("Animals are make sounds")

class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")

class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof! Woof!")

cat = Cat()
print("\n---Cat Sound---")
cat.make_sound()
dog = Dog()
print("\n---Dog Sound---")
dog.make_sound()
