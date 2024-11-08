class Car:
    def __init__(self, plate_number, colour):
        self.plate_number = plate_number
        self.colour = colour

class PaintShop:
    def paint(self, car, colour):
        car.colour = colour

paint_shop = PaintShop()
car = Car("10-LZ-126", "blue")
print(f"The car is {car.colour}")
paint_shop.paint(car, "red")
print(f"The car is now {car.colour}")