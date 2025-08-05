class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Polymorphism in action
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
