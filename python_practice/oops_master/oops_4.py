class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    def habitat(self):
        raise NotImplementedError("Subclasses must implement this method")


class Lion(Animal):
    def speak(self):
        return "Roar"

    def habitat(self):
        return "Savanna"


class Elephant(Animal):
    def speak(self):
        return "Trumpet"

    def habitat(self):
        return "Forest"


class Zoo:  # No inheritance from Animal
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):  # Check if the object is an Animal instance
            self.animals.append(animal)
        else:
            print(f"Cannot add {type(animal)}. It must be an Animal instance.")

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name}: {animal.speak()} (Habitat: {animal.habitat()})")


# Creating animal instances
simba = Lion("Simba")
dumbo = Elephant("Dumbo")

# Creating a zoo
my_zoo = Zoo()

# Adding animals to the zoo
my_zoo.add_animal(simba)
my_zoo.add_animal(dumbo)

# Displaying animals in the zoo
my_zoo.display_animals()
