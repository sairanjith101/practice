# 2.4 Class / Static / Instance Methods

class Demo:
    count = 0

    def __init__(self):
        Demo.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        print("Hello!")

d1 = Demo()
d2 = Demo()
print(d1.get_count())
d2.geet()