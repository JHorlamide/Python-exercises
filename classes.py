class Person():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, my name in {self.name}")

person1 = Person('JHorlamide')

print(person1.name)

person1.talk()