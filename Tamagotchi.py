class Tamagotchi:
    def __init__(self, stat, hunger, happiness, training, sickness, age, weight):
        self.stat = stat
        self.hunger = hunger
        self.happiness = happiness
        self.training = training
        self.sickness = sickness
        self.age = age
        self.weight = weight
    def GetAge(self):
        return self.age
    def GetWeight(self):
        return self.weight
    def Eat(self, food):
        self.hunger -= 1
        self.weight += 1
        self.sickness -= 1
    def MiniGame(self):
        self.hunger += 1
        self.happiness += 1
        self.training += 1
    def Sleep(self, hours):
        self.sickness -= hours
        self.happiness += hours

