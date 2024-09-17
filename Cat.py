from Tamagotchi import *
class Cat(Tamagotchi):
    def __init__(self, stat, hunger, hapiness, training, sickness, age, weight, type, nails, washed):
        Tamagotchi.__init__(stat, hunger+2, hapiness-10, training-3, sickness, age, weight-2)
        self.type = type
        self.nails = nails
        self.washed = washed

    def Scratch(self, amount):
        self.nails += amount
        self.training += (amount/3)

    def Wash(self):
        self.washed = 10
        self.sickness += 1
