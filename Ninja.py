from Tamagotchi import *
class Ninja(Tamagotchi):
    # init function
    def __init__(self, stat, hunger, happiness, training, sickness, age, weight, weapon, weapon_lvl):
        Tamagotchi.__init__(stat, hunger-5, happiness-2, training+5, sickness-2, age, weight+10)
        self.weapon = weapon
    def Mission(self, lvl):
        self.hunger += lvl*3
        self.training += lvl*5
        self.sickness += lvl*2
        lst_of_weapons = ['bow', 'crossbow', 'knife', 'shurikans', 'sword', 'hammer', 'scythe', 'spear', 'axe', 'boomerang', 'stick']





