from virtual_pet import VirtualPet


class Cat(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Cat"

    def meow(self):
        print(f"{self.name} says: Meow!")
