
from src.headers import *
from colorama import init, Fore, Back, Style
import math
import numpy as np
init()


class Buildings:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def clear(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = " "


class TownHall(Buildings):
    def __init__(self, x, y):
        self.height = 3
        self.width = 4
        self.max_health = 500
        self.health = 500
        self.destroyed = 0
        Buildings.__init__(self, x, y)

    def place_TH(self, grid):
        x = self.get_x()
        y = self.get_y()

        # print(x, y)
        max_x = x + self.width
        max_y = y + self.height
        for j in range(x, max_x):
            grid[y][j] = Fore.BLACK+Back.CYAN + "-"+Style.RESET_ALL
            grid[max_y-1][j] = Fore.BLACK+Back.CYAN + "-"+Style.RESET_ALL
        for i in range(y, max_y):
            grid[i][x] = Fore.BLACK+Back.CYAN + "|"+Style.RESET_ALL
            grid[i][max_x-1] = Fore.BLACK+Back.CYAN + "|"+Style.RESET_ALL

        grid[y+1][x+1] = Fore.BLACK+Back.CYAN + "T"+Style.RESET_ALL
        grid[y+1][x+2] = Fore.BLACK+Back.CYAN + "H"+Style.RESET_ALL

    def clear(self, grid):
        x = self.get_x()
        y = self.get_y()

        for i in range(x, x+self.width):
            for j in range(y, y+self.height):
                grid[j][i] = " "

    def update_TH(self, grid):
        x = self.get_x()
        y = self.get_y()
        max_x = x + self.width
        max_y = y + self.height

        if(self.health > self.max_health/2):
            for j in range(x, max_x):
                grid[y][j] = Fore.BLACK+Back.CYAN + "-"+Style.RESET_ALL
                grid[max_y-1][j] = Fore.BLACK+Back.CYAN + "-"+Style.RESET_ALL
            for i in range(y, max_y):
                grid[i][x] = Fore.BLACK+Back.CYAN + "|"+Style.RESET_ALL
                grid[i][max_x-1] = Fore.BLACK+Back.CYAN + "|"+Style.RESET_ALL

            grid[y+1][x+1] = Fore.BLACK+Back.CYAN + "T"+Style.RESET_ALL
            grid[y+1][x+2] = Fore.BLACK+Back.CYAN + "H"+Style.RESET_ALL

        elif(self.health > self.max_health/5):

            for j in range(x, max_x):
                grid[y][j] = Fore.BLACK+Back.YELLOW + "-"+Style.RESET_ALL
                grid[max_y-1][j] = Fore.BLACK+Back.YELLOW + "-"+Style.RESET_ALL
            for i in range(y, max_y):
                grid[i][x] = Fore.BLACK+Back.YELLOW + "|"+Style.RESET_ALL
                grid[i][max_x-1] = Fore.BLACK+Back.YELLOW + "|"+Style.RESET_ALL

            grid[y+1][x+1] = Fore.BLACK+Back.YELLOW + "T"+Style.RESET_ALL
            grid[y+1][x+2] = Fore.BLACK+Back.YELLOW + "H"+Style.RESET_ALL

        elif(self.health > 0):

            for j in range(x, max_x):
                grid[y][j] = Fore.BLACK+Back.RED + "-"+Style.RESET_ALL
                grid[max_y-1][j] = Fore.BLACK+Back.RED + "-"+Style.RESET_ALL
            for i in range(y, max_y):
                grid[i][x] = Fore.BLACK+Back.RED + "|"+Style.RESET_ALL
                grid[i][max_x-1] = Fore.BLACK+Back.RED + "|"+Style.RESET_ALL

            grid[y+1][x+1] = Fore.BLACK+Back.RED + "T"+Style.RESET_ALL
            grid[y+1][x+2] = Fore.BLACK+Back.RED + "H"+Style.RESET_ALL

        else:
            self.clear(grid)


class Hut(Buildings):
    def __init__(self, x, y):
        self.max_health = 250
        self.health = 250
        super().__init__(x, y)

    def place_hut(self, grid):
        x = self.get_x()
        y = self.get_y()

        # print(x,y)
        grid[y][x] = Back.MAGENTA + Fore.WHITE + "H" + Style.RESET_ALL

    def update_hut(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.health > self.max_health/2):
            grid[y][x] = Back.MAGENTA + Fore.WHITE + "H" + Style.RESET_ALL
        elif(self.health > self.max_health/5):
            grid[y][x] = Back.YELLOW + Fore.BLACK + "H" + Style.RESET_ALL
        elif(self.health > 0):
            grid[y][x] = Back.RED + Fore.BLACK + "H" + Style.RESET_ALL
        else:
            self.clear(grid)


class Walls(Buildings):
    def __init__(self, x, y):
        self.max_health = 1000
        self.health = 1000
        super().__init__(x, y)

    def place_wall(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = Back.LIGHTBLACK_EX + Fore.WHITE + "W" + Style.RESET_ALL

    def update_wall(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.health > self.max_health/2):
            grid[y][x] = Back.LIGHTBLACK_EX + \
                Fore.WHITE + "W" + Style.RESET_ALL
        elif(self.health > self.max_health/5):
            grid[y][x] = Back.YELLOW + Fore.BLACK + "W" + Style.RESET_ALL
        elif(self.health > 0):
            grid[y][x] = Back.RED + Fore.BLACK + "W" + Style.RESET_ALL
        else:
            self.clear(grid)


class Cannon(Buildings):
    def __init__(self, x, y):
        self.max_health = 300
        self.health = 300
        self.attack_damage = 30
        self.attac = 0
        self.body = np.array([Back.BLUE + Fore.WHITE+"-" + Style.RESET_ALL, Back.BLUE +
                             Fore.WHITE+"C" + Style.RESET_ALL, Back.BLUE + Fore.WHITE+"-" + Style.RESET_ALL])
        super().__init__(x, y)

    def place_cannon(self, grid):
        x = self.get_x()
        y = self.get_y()

        for i in range(x-1, x+2):
            grid[y][i] = self.body[i - (x-1)]

    def clear_cannon(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x-1] = " "
        grid[y][x] = " "
        grid[y][x+1] = " "

    def update_cannon(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.attac == 0):
            if(self.health > self.max_health/2):
                self.body = np.array([Back.BLUE + Fore.WHITE+"-" + Style.RESET_ALL, Back.BLUE +
                                      Fore.WHITE+"C" + Style.RESET_ALL, Back.BLUE + Fore.WHITE+"-" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > self.max_health/5):
                self.body = np.array([Back.YELLOW + Fore.BLACK+"-" + Style.RESET_ALL, Back.YELLOW +
                                      Fore.BLACK+"C" + Style.RESET_ALL, Back.YELLOW + Fore.BLACK+"-" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > 0):
                self.body = np.array([Back.RED + Fore.BLACK+"-" + Style.RESET_ALL, Back.RED +
                                      Fore.BLACK+"C" + Style.RESET_ALL, Back.RED + Fore.BLACK+"-" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            else:
                self.clear_cannon(grid)
        if(self.attac == 1):
            if(self.health > self.max_health/2):
                self.body = np.array([Back.BLUE + Fore.BLACK+"*" + Style.RESET_ALL, Back.BLUE +
                                      Fore.WHITE+"C" + Style.RESET_ALL, Back.BLUE + Fore.BLACK+"*" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > self.max_health/5):
                self.body = np.array([Back.YELLOW + Fore.BLUE+"*" + Style.RESET_ALL, Back.YELLOW +
                                      Fore.BLACK+"C" + Style.RESET_ALL, Back.YELLOW + Fore.BLUE+"*" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > 0):
                self.body = np.array([Back.RED + Fore.BLUE+"*" + Style.RESET_ALL, Back.RED +
                                      Fore.BLACK+"C" + Style.RESET_ALL, Back.RED + Fore.BLUE+"*" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            else:
                self.clear_cannon(grid)

    def fire_cannon(self, grid, Hero):
        min_dist = 100
        index = -1
        flag = -1

        for i in range(len(Barbarian_arr)):
            x_dist = Barbarian_arr[i].get_x() - self.get_x()
            y_dist = Barbarian_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 1
                index = i
                min_dist = dist

        for i in range(len(Archer_arr)):
            x_dist = Archer_arr[i].get_x() - self.get_x()
            y_dist = Archer_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 3
                index = i
                min_dist = dist

        if(Hero.alive == 1):
            King_x_dist = Hero.get_x() - self.get_x()
            King_y_dist = Hero.get_y() - self.get_y()

            dist = math.sqrt(King_x_dist**2 + King_y_dist**2)
            if(dist < min_dist):
                index = -5
                flag = 4
                min_dist = dist

        if(min_dist < 8):
            self.attac = 1
            if(flag == 4):
                Hero.health = Hero.health - self.attack_damage
                if(Hero.health <= 0):
                    Hero.clear_hero(
                        grid, Hero.get_x(), Hero.get_y())
                    Hero.alive = 0

            if(flag == 1):
                Barbarian_arr[index].health = Barbarian_arr[index].health - \
                    self.attack_damage
                Barbarian_arr[index].update_barbarian_stats(grid)
                if(Barbarian_arr[index].health <= 0):
                    Barbarian_arr.pop(index)

            if(flag == 3):
                Archer_arr[index].health = Archer_arr[index].health - \
                    self.attack_damage
                Archer_arr[index].update_archer_stats(grid)
                if(Archer_arr[index].health <= 0):
                    Archer_arr.pop(index)

        else:
            self.attac = 0


class Wizard_Tower(Buildings):
    def __init__(self, x, y):
        self.max_health = 300
        self.health = 300
        self.attack_damage = 30
        self.attac = 0
        self.body = np.array([Back.LIGHTMAGENTA_EX + Fore.WHITE+"-" + Style.RESET_ALL, Back.LIGHTMAGENTA_EX +
                             Fore.WHITE+"T" + Style.RESET_ALL, Back.LIGHTMAGENTA_EX + Fore.WHITE+"-" + Style.RESET_ALL])
        super().__init__(x, y)

    def place_wizard_tower(self, grid):
        x = self.get_x()
        y = self.get_y()

        for i in range(x-1, x+2):
            grid[y][i] = self.body[i - (x-1)]

    def clear_wizard_tower(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x-1] = " "
        grid[y][x] = " "
        grid[y][x+1] = " "

    def update_wizard_tower(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.attac == 0):
            if(self.health > self.max_health/2):
                self.body = np.array([Back.LIGHTMAGENTA_EX + Fore.WHITE+"-" + Style.RESET_ALL, Back.LIGHTMAGENTA_EX +
                                      Fore.WHITE+"T" + Style.RESET_ALL, Back.LIGHTMAGENTA_EX + Fore.WHITE+"-" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > self.max_health/5):
                self.body = np.array([Back.YELLOW + Fore.BLACK+"-" + Style.RESET_ALL, Back.YELLOW +
                                      Fore.BLACK+"T" + Style.RESET_ALL, Back.YELLOW + Fore.BLACK+"-" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > 0):
                self.body = np.array([Back.RED + Fore.BLACK+"-" + Style.RESET_ALL, Back.RED +
                                      Fore.BLACK+"T" + Style.RESET_ALL, Back.RED + Fore.BLACK+"-" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            else:
                self.clear_wizard_tower(grid)
        if(self.attac == 1):
            if(self.health > self.max_health/2):
                self.body = np.array([Back.LIGHTMAGENTA_EX + Fore.BLACK+"*" + Style.RESET_ALL, Back.LIGHTMAGENTA_EX +
                                      Fore.WHITE+"T" + Style.RESET_ALL, Back.LIGHTMAGENTA_EX + Fore.BLACK+"*" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > self.max_health/5):
                self.body = np.array([Back.YELLOW + Fore.BLUE+"*" + Style.RESET_ALL, Back.YELLOW +
                                      Fore.BLACK+"T" + Style.RESET_ALL, Back.YELLOW + Fore.BLUE+"*" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            elif(self.health > 0):
                self.body = np.array([Back.RED + Fore.BLUE+"*" + Style.RESET_ALL, Back.RED +
                                      Fore.BLACK+"T" + Style.RESET_ALL, Back.RED + Fore.BLUE+"*" + Style.RESET_ALL])
                for i in range(x-1, x+2):
                    grid[y][i] = self.body[i - (x-1)]
            else:
                self.clear_wizard_tower(grid)

    def fire_wizard_tower(self, grid, Hero):
        min_dist = 100
        index = -1
        flag = -1

        for i in range(len(Barbarian_arr)):
            x_dist = Barbarian_arr[i].get_x() - self.get_x()
            y_dist = Barbarian_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 1
                index = i
                min_dist = dist

        for i in range(len(Baloon_arr)):
            x_dist = Baloon_arr[i].get_x() - self.get_x()
            y_dist = Baloon_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 2
                index = i
                min_dist = dist

        for i in range(len(Archer_arr)):
            x_dist = Archer_arr[i].get_x() - self.get_x()
            y_dist = Archer_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 3
                index = i
                min_dist = dist

        if(Hero.alive == 1):
            King_x_dist = Hero.get_x() - self.get_x()
            King_y_dist = Hero.get_y() - self.get_y()

            dist = math.sqrt(King_x_dist**2 + King_y_dist**2)
            if(dist < min_dist):
                flag = 4
                index = -5
                min_dist = dist

        if(min_dist <= 8):
            self.attac = 1
            if(flag == 4):
                x = Hero.get_x()
                y = Hero.get_y()
                Wizard_tower_attac(grid, x, y, Hero, self.attack_damage)
            elif(flag == 1):
                x = Barbarian_arr[index].get_x()
                y = Barbarian_arr[index].get_y()
                Wizard_tower_attac(grid, x, y, Hero, self.attack_damage)
            elif(flag == 2):
                x = Baloon_arr[index].get_x()
                y = Baloon_arr[index].get_y()
                Wizard_tower_attac(grid, x, y, Hero, self.attack_damage)
            elif(flag == 3):
                x = Archer_arr[index].get_x()
                y = Archer_arr[index].get_y()
                Wizard_tower_attac(grid, x, y, Hero, self.attack_damage)

        else:
            self.attac = 0


def Wizard_tower_attac(grid, x, y, Hero, damage):
    if(Hero.alive == 1):
        x_val = Hero.get_x()
        y_val = Hero.get_y()
        if(x_val >= x-1 and x_val <= x+1 and y_val >= y-1 and y_val <= y+1):
            Hero.health = Hero.health - damage
            if(Hero.health <= 0):
                Hero.clear_hero(
                    grid, Hero.get_x(), Hero.get_y())
                Hero.alive = 0

    for barb in Barbarian_arr:
        x_val = barb.get_x()
        y_val = barb.get_y()
        if(x_val >= x-1 and x_val <= x+1 and y_val >= y-1 and y_val <= y+1):
            barb.health = barb.health - damage
            barb.update_barbarian_stats(grid)
            if(barb.health <= 0):
                Barbarian_arr.pop(Barbarian_arr.index(barb))

    for baloon in Baloon_arr:
        x_val = baloon.get_x()
        y_val = baloon.get_y()
        if(x_val >= x-1 and x_val <= x+1 and y_val >= y-1 and y_val <= y+1):
            baloon.health = baloon.health - damage
            baloon.update_baloon_stats(grid)
            if(baloon.health <= 0):
                Baloon_arr.pop(Baloon_arr.index(baloon))

    for archer in Archer_arr:
        x_val = archer.get_x()
        y_val = archer.get_y()
        if(x_val >= x-1 and x_val <= x+1 and y_val >= y-1 and y_val <= y+1):
            archer.health = archer.health - damage
            archer.update_archer_stats(grid)
            if(archer.health <= 0):
                Archer_arr.pop(Archer_arr.index(archer))


class Spawn(Buildings):
    def __init__(self, x, y, ch, troops1, troops2, troops3):
        self.body = str(ch)
        self.barbarians = troops1
        self.baloons = troops2
        self.archers = troops3
        super().__init__(x, y)

    def place_spawner(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = Back.GREEN + Fore.BLACK + self.body + Style.RESET_ALL
