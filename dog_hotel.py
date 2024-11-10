class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birt_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(f"{self.name} barks: {self.sound}")
        return
    
class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(f"{dog.name} checked in.")
        return
    
    def dog_chekout(self, dog):
        self.dogs.remove(dog)
        print(f"{dog.name} checked out.")

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

dog1 = Dog("Tula", "2018")
dog2 = Dog("Yalaq", "2020", "Haw Haw")

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

hotel.dog_chekout(dog2)
hotel.greet_dogs()
