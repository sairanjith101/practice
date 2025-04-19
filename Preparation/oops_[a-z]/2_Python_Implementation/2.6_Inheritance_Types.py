# Single Inheritance

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Multiple Inheritance

class A:
    def feature1(self):
        print("Feature 1")

class B:
    def feature2(self):
        print("Feature 2")

class C(A, B):
    pass