from Tamagotchi import *
class Alien(Tamagotchi):
    def __init__(self, stat, hunger, hapiness, training, sickness, age, weight, horns, tail, eyes):
        Tamagotchi.__init__(stat, hunger+2, hapiness-10, training-3, sickness, age, weight-2)
        self.horns = horns
        self.tail = tail
        self.eyes = eyes

    def Laser_eyes(self, amount):
        self.eyes += amount
        self.training += (amount/2)

    def Run(self):
        self.training +=1
        self.hapiness -=1
