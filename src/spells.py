from src.headers import *


class Spells:
    def __init__(self):
        pass

    def cast_spell(self):
        pass


class Rage(Spells):
    def __init__(self):
        self._time = 3
        self.number = 2
        self.active = 0
        self.start = -100
        super().__init__()

    def cast_spell(self, fr):
        self.active = 1
        self.start = fr


class Heal(Spells):
    def __init__(self):
        self.factor = 1.5
        self.number = 2
        super().__init__()

    def cast_spell(self, Hero):
        for i in range(len(Barbarian_arr)):
            Barbarian_arr[i].health = (Barbarian_arr[i].health*self.factor)
            if(Barbarian_arr[i].health > Barbarian_arr[i].max_health):
                Barbarian_arr[i].health = Barbarian_arr[i].max_health

        # print(Hero.health, self.factor)
        if(Hero.alive == 1):
            Hero.health = (Hero.health*self.factor)
            if(Hero.health > Hero.max_health):
                Hero.health = Hero.max_health

        for i in range(len(Archer_arr)):
            Archer_arr[i].health = (Archer_arr[i].health*self.factor)
            if(Archer_arr[i].health > Archer_arr[i].max_health):
                Archer_arr[i].health = Archer_arr[i].max_health

        for i in range(len(Baloon_arr)):
            Baloon_arr[i].health = (Baloon_arr[i].health*self.factor)
            if(Baloon_arr[i].health > Baloon_arr[i].max_health):
                Baloon_arr[i].health = Baloon_arr[i].max_health
