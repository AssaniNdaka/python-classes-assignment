# Base class
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.__strength = strength  # Encapsulated attribute

    def show_power(self):
        return f"{self.name} uses {self.power}!"

    def get_strength(self):
        return self.__strength

    def set_strength(self, value):
        if value > 0:
            self.__strength = value
        else:
            print("Strength must be positive!")

# Derived class (Inheritance + Polymorphism)
class FlyingSuperhero(Superhero):
    def show_power(self):
        return f"{self.name} flies through the sky using {self.power}! 🦸‍♂️"

# Example
hero1 = Superhero("Storm", "Weather Control", 90)
hero2 = FlyingSuperhero("Falcon", "Wings", 80)

print(hero1.show_power())
print(f"Strength: {hero1.get_strength()}")

print(hero2.show_power())
print(f"Strength: {hero2.get_strength()}")
