class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.happiness = 50
        self.hunger = 50
        self.cleanliness = 50
        self.sleep_counter = 0  # Counter to track sleep actions

    @property
    def is_alive(self):
        return self.happiness > 0 and self.hunger > 0

    def feed(self):
        if self.hunger < 100:
            self.hunger += 20
            self.happiness += 5
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 15
            self.cleanliness -= 10
            print(f"{self.name} played and is now happier!")
        else:
            print(f"{self.name} is already very happy!")

    def groom(self):
        self.cleanliness += 20
        self.happiness += 10
        print(f"{self.name} has been groomed!")

    def sleep(self):
        self.sleep_counter += 1  # Increment the sleep counter
        self.happiness += 10
        self.cleanliness -= 5
        print(f"{self.name} fell asleep.")
        print(f"{self.name} woke up!.")

        # Check if it's time to age the pet
        if self.sleep_counter >= 7:  # If the pet has slept 7 times
            self.age += 1  # Increase age by 1
            self.sleep_counter = 0  # Reset the sleep counter
            print(f"{self.name} is now {self.age} years old!")

    def display_status(self):
        print(f"Name: {self.name}, Age: {self.age}, Happiness: {self.happiness}, Hunger: {self.hunger}, Cleanliness: {self.cleanliness}")
