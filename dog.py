from virtual_pet import VirtualPet


class Dog(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Dog"

    def bark(self):
        print(f"{self.name} says: Woof!")
