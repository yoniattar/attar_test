from virtual_pet import VirtualPet


class Parrot(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Parrot"

    def repeat(self):
        sentence = input(f"say something to {self.name}!").lower()
        print(f"{self.name} says:", sentence, "!")