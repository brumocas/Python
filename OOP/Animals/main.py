class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound():
        pass

    def print(self):
        print("Name:", self.name)

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")


cat1 = Cat("Garfield")
cat1.print()
cat1.make_sound()


dog1 = Dog("Max")
dog1.print()
dog1.make_sound()

