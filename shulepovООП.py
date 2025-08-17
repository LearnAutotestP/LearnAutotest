class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} говорит"


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def make_sound(self):
        parent_make_sound = super().make_sound()
        return f"{parent_make_sound}, {self.sound}"


class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def make_sound(self):
        parent_make_sound = super().make_sound()
        return f"{parent_make_sound}, {self.sound}"


class Cow(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def make_sound(self):
        parent_make_sound = super().make_sound()
        return f"{parent_make_sound}, {self.sound}"


dog = Dog("Собака Ворчун", "Гав-Гав")
cat = Cat("Кошка Мурка", "Мяу-Бля")
cow = Cow("Корова Тварь", "Муу-сука")

print(dog.name)
print(cat.name)
print(cow.name)
print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())