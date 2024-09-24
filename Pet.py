from Tamagotchi import *
class Pet(Tamagotchi):
    def __init__(self, stat, hunger, happiness, training, sickness, age, weight):
        Tamagotchi.__init__(stat, hunger + 2 , happiness + 4, training + 2, sickness - 2, age, weight + 5)
    def PLAY(self):
        self.happiness += 5
        self.hunger += 3
    def Exercise(self):
        self.hunger += 3
        self.training += 5
        self.weight += 1
    def SLEEP(self):
        self.happiness += 2
        self.sickness -= 4
    def EAT(self):
        self.hunger -= 5
