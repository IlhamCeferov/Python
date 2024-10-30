class Dog:

    created = 0

    def __init__(self, name, birth_year, sound = "woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created += 1

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return
    
dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "yip yip yip")

dog1.bark(2)
dog2.bark(3)

print(f"{Dog.created} dogs have been created.")