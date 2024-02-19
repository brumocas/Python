class Fruit:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def print(self):
        print(f"{self.name} ({self.number})")

    def update(self, new_number):
        self.number = new_number


a1 = Fruit("Banana", 10)
a1.print()

a2 = Fruit("Apple", 7)
a2.update(12)
a2.print()


