from src.headers import *
from src.village import *
from src.initialise import *
from colorama import init, Fore, Back, Style
import numpy as np
import math
import threading
from time import sleep
init()


class Troops:
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


class King(Troops):
    def __init__(self, x, y):
        self._body = np.array([[" ", "0", " "], [
                              "/", Back.RED+Fore.WHITE + "K" + Style.RESET_ALL, "\\"], ["/", " ", "\\"]])
        self.max_health = 1500
        self.health = 1500
        self.attack_damage = 100
        self.range = 5
        self.alive = 1
        super().__init__(x, y)

    def place_hero(self, grid):
        x = self.get_x()
        y = self.get_y()

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                grid[j][i] = self._body[j-(y-1)][i-(x-1)]

    def clear_hero(self, grid, x, y):

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                grid[j][i] = " "

    def move_up(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(y > 2 and grid[y-2][x] == ' ' and grid[y-2][x-1] == ' ' and grid[y-2][x+1] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_y(y-1)
            y = y-1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]

    def move_down(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(y < HEIGHT-3 and grid[y+2][x] == ' ' and grid[y+2][x-1] == ' ' and grid[y+2][x+1] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_y(y+1)
            y = y+1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]

    def move_left(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(x > 2 and grid[y][x-2] == ' ' and grid[y-1][x-2] == ' ' and grid[y+1][x-2] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_x(x-1)
            x = x-1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]

    def move_right(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(x < WIDTH-3 and grid[y][x+2] == ' ' and grid[y-1][x+2] == ' ' and grid[y+1][x+2] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_x(x+1)
            x = x+1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]

    def attack(self, grid, Town_hall):
        for i in range(len(Huts_arr)):
            x_dist = Huts_arr[i].get_x() - self.get_x()
            y_dist = Huts_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.range):
                Huts_arr[i].health = Huts_arr[i].health - self.attack_damage

        for i in range(len(Walls_arr)):
            x_dist = Walls_arr[i].get_x() - self.get_x()
            y_dist = Walls_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.range):
                Walls_arr[i].health = Walls_arr[i].health - self.attack_damage

        for i in range(len(Cannon_arr)):
            x_dist = Cannon_arr[i].get_x() - self.get_x()
            y_dist = Cannon_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.range):
                Cannon_arr[i].health = Cannon_arr[i].health - \
                    self.attack_damage

        for i in range(len(Wizard_tower_arr)):
            x_dist = Wizard_tower_arr[i].get_x() - self.get_x()
            y_dist = Wizard_tower_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.range):
                Wizard_tower_arr[i].health = Wizard_tower_arr[i].health - \
                    self.attack_damage

        if(Town_hall.destroyed == 0):
            x_dist = Town_hall.get_x() - self.get_x()
            y_dist = Town_hall.get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.range):
                Town_hall.health = Town_hall.health - self.attack_damage


class Queen(Troops):
    def __init__(self, x, y):
        self._body = np.array([["/", "0", "\\"], [
                              "/", Back.RED+Fore.WHITE + "Q" + Style.RESET_ALL, "\\"], ["/", " ", "\\"]])
        self.max_health = 1200
        self.health = 1200
        self.attack_damage = 60
        self.range = 8
        self.attack_radius = 5
        self.alive = 1
        self.last_dir = 'right'
        super().__init__(x, y)

    def place_hero(self, grid):
        x = self.get_x()
        y = self.get_y()

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                grid[j][i] = self._body[j-(y-1)][i-(x-1)]

    def clear_hero(self, grid, x, y):

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                grid[j][i] = " "

    def move_up(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(y > 2 and grid[y-2][x] == ' ' and grid[y-2][x-1] == ' ' and grid[y-2][x+1] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_y(y-1)
            y = y-1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]
            self.last_dir = 'up'

    def move_down(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(y < HEIGHT-3 and grid[y+2][x] == ' ' and grid[y+2][x-1] == ' ' and grid[y+2][x+1] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_y(y+1)
            y = y+1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]
            self.last_dir = 'down'

    def move_left(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(x > 2 and grid[y][x-2] == ' ' and grid[y-1][x-2] == ' ' and grid[y+1][x-2] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_x(x-1)
            x = x-1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]

            self.last_dir = 'left'

    def move_right(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(x < WIDTH-3 and grid[y][x+2] == ' ' and grid[y-1][x+2] == ' ' and grid[y+1][x+2] == ' '):
            self.clear_hero(grid, x, y)
            sleep(0.03)
            self.set_x(x+1)
            x = x+1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    grid[j][i] = self._body[j-(y-1)][i-(x-1)]

            self.last_dir = 'right'

    def attack(self, grid, Town_hall):
        x = self.get_x()
        y = self.get_y()

        if(self.last_dir == 'right'):
            x = x + self.range

        if(self.last_dir == 'left'):
            x = x - self.range

        if(self.last_dir == 'up'):
            y = y - self.range

        if(self.last_dir == 'down'):
            y = y + self.range

        for i in range(len(Cannon_arr)):
            x_dist = Cannon_arr[i].get_x() - x
            y_dist = Cannon_arr[i].get_y() - y

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.attack_radius):
                Cannon_arr[i].health = Cannon_arr[i].health - \
                    self.attack_damage

        for i in range(len(Wizard_tower_arr)):
            x_dist = Wizard_tower_arr[i].get_x() - x
            y_dist = Wizard_tower_arr[i].get_y() - y

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.attack_radius):
                Wizard_tower_arr[i].health = Wizard_tower_arr[i].health - \
                    self.attack_damage

        if(Town_hall.destroyed == 0):
            x_dist = Town_hall.get_x() - x
            y_dist = Town_hall.get_y() - y

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.attack_radius):
                Town_hall.health = Town_hall.health - self.attack_damage

        for i in range(len(Huts_arr)):
            x_dist = Huts_arr[i].get_x() - x
            y_dist = Huts_arr[i].get_y() - y

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.attack_radius):
                Huts_arr[i].health = Huts_arr[i].health - self.attack_damage

        for i in range(len(Walls_arr)):
            x_dist = Walls_arr[i].get_x() - x
            y_dist = Walls_arr[i].get_y() - y

            dist = math.sqrt(x_dist**2 + y_dist**2)

            if(dist <= self.attack_radius):
                Walls_arr[i].health = Walls_arr[i].health - self.attack_damage

    def eagle_arrow_attack(self, grid, Town_hall):
        x = self.get_x()
        y = self.get_y()

        if(self.last_dir == 'right'):
            x = x + 16

        if(self.last_dir == 'left'):
            x = x - 16

        if(self.last_dir == 'up'):
            y = y - 16

        if(self.last_dir == 'down'):
            y = y + 16

        # start_time = threading.Timer(1,EagleArrow(x,y,self.attack_damage))
        # start_time.start()
        # EagleArrow(x,y,self.attack_damage,Town_hall)
        QueenEagleEye.append(x)
        QueenEagleEye.append(y)
        QueenEagleEye.append(self.attack_damage)


def EagleArrow(x, y, damage, Town_hall):
    for i in range(len(Cannon_arr)):
        x_dist = Cannon_arr[i].get_x() - x
        y_dist = Cannon_arr[i].get_y() - y

        dist = math.sqrt(x_dist**2 + y_dist**2)

        if(dist <= 9):
            Cannon_arr[i].health = Cannon_arr[i].health - \
                damage

    for i in range(len(Wizard_tower_arr)):
        x_dist = Wizard_tower_arr[i].get_x() - x
        y_dist = Wizard_tower_arr[i].get_y() - y

        dist = math.sqrt(x_dist**2 + y_dist**2)

        if(dist <= 9):
            Wizard_tower_arr[i].health = Wizard_tower_arr[i].health - \
                damage

    if(Town_hall.destroyed == 0):
        x_dist = Town_hall.get_x() - x
        y_dist = Town_hall.get_y() - y

        dist = math.sqrt(x_dist**2 + y_dist**2)

        if(dist <= 9):
            Town_hall.health = Town_hall.health - damage

    for i in range(len(Huts_arr)):
        x_dist = Huts_arr[i].get_x() - x
        y_dist = Huts_arr[i].get_y() - y

        dist = math.sqrt(x_dist**2 + y_dist**2)

        if(dist <= 9):
            Huts_arr[i].health = Huts_arr[i].health - damage

    for i in range(len(Walls_arr)):
        x_dist = Walls_arr[i].get_x() - x
        y_dist = Walls_arr[i].get_y() - y

        dist = math.sqrt(x_dist**2 + y_dist**2)

        if(dist <= 9):
            Walls_arr[i].health = Walls_arr[i].health - damage


# for troop attack
def strike(x_val, y_val, attack, grid, Town_hall):

    for wall in Walls_arr:
        x = wall.get_x()
        y = wall.get_y()
        if(x == x_val and y == y_val):
            wall.health = wall.health - attack
            wall.update_wall(grid)
            if(wall.health <= 0):
                wall.clear(grid)
                Walls_arr.remove(wall)

    for hut in Huts_arr:
        x = hut.get_x()
        y = hut.get_y()
        if(x == x_val and y == y_val):
            hut.health = hut.health - attack
            hut.update_hut(grid)
            if(hut.health <= 0):
                hut.clear(grid)
                Huts_arr.remove(hut)

    for cannon in Cannon_arr:
        x = cannon.get_x()
        y = cannon.get_y()
        if(y == y_val and (x == x_val or x-1 == x_val or x+1 == x_val)):
            cannon.health = cannon.health - attack
            cannon.update_cannon(grid)
            if(cannon.health <= 0):
                cannon.clear_cannon(grid)
                Cannon_arr.remove(cannon)

    for wizardTower in Wizard_tower_arr:
        x = wizardTower.get_x()
        y = wizardTower.get_y()
        if(y == y_val and (x == x_val or x-1 == x_val or x+1 == x_val)):
            wizardTower.health = wizardTower.health - attack
            wizardTower.update_wizard_tower(grid)
            if(wizardTower.health <= 0):
                wizardTower.clear_wizard_tower(grid)
                Wizard_tower_arr.remove(wizardTower)

    if(Town_hall.destroyed == 0):
        x = Town_hall.get_x()
        y = Town_hall.get_y()
        # print(x,y)
        if(y_val >= y and y_val <= y+2 and x_val >= x and x_val <= x+3):
            Town_hall.health = Town_hall.health - attack


class Barbarian(Troops):
    def __init__(self, x, y):
        self.max_health = 80
        self.health = 80
        self.attack_damage = 20
        super().__init__(x, y)

    def place_barbarian(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = Back.YELLOW + Fore.BLACK + "B" + Style.RESET_ALL

    def clear_barbarian(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = " "

    def update_barbarian_stats(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.health > 50):
            grid[y][x] = Back.YELLOW + Fore.BLACK + "B" + Style.RESET_ALL
        elif(self.health > 20):
            grid[y][x] = Back.LIGHTYELLOW_EX + \
                Fore.BLACK + "B" + Style.RESET_ALL
        elif(self.health > 0):
            grid[y][x] = Back.LIGHTRED_EX + Fore.BLACK + "B" + Style.RESET_ALL
        else:
            self.clear_barbarian(grid)

    def update_barb(self, grid, Town_hall):
        min_dist = 100
        flag = -1
        index = -1

        for i in range(len(Huts_arr)):
            x_dist = Huts_arr[i].get_x() - self.get_x()
            y_dist = Huts_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 1
                index = i
                min_dist = dist

        for i in range(len(Cannon_arr)):
            x_dist = Cannon_arr[i].get_x() - self.get_x()
            y_dist = Cannon_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 2
                index = i
                min_dist = dist

        for i in range(len(Wizard_tower_arr)):
            x_dist = Wizard_tower_arr[i].get_x() - self.get_x()
            y_dist = Wizard_tower_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 4
                index = i
                min_dist = dist

        if(Town_hall.destroyed == 0):
            TH_x_dist = Town_hall.get_x() - self.get_x()
            TH_y_dist = Town_hall.get_y() - self.get_y()

            dist = math.sqrt(TH_x_dist**2 + TH_y_dist**2)
            if(dist < min_dist):
                flag = 3
                min_dist = dist

        # print('flagg',flag)
        x_val = self.get_x()
        y_val = self.get_y()

        x_diff = 0
        y_diff = 0

        if(flag == 1):
            x_diff = Huts_arr[index].get_x() - x_val
            y_diff = Huts_arr[index].get_y() - y_val

        if(flag == 2):
            x_diff = Cannon_arr[index].get_x() - x_val
            y_diff = Cannon_arr[index].get_y() - y_val

        if(flag == 3):
            x_diff = Town_hall.get_x()+1 - x_val
            y_diff = Town_hall.get_y()+1 - y_val

        if(flag == 4):
            x_diff = Wizard_tower_arr[index].get_x() - x_val
            y_diff = Wizard_tower_arr[index].get_y() - y_val

        if(abs(x_diff) > abs(y_diff)):
            if(x_diff > 0):
                if(grid[y_val][x_val+1] == ' '):

                    self.clear_barbarian(grid)

                    self.set_x(x_val+1)
                    self.update_barbarian_stats(grid)
                else:
                    strike(x_val+1, y_val, self.attack_damage, grid, Town_hall)
            if(x_diff < 0):
                if(grid[y_val][x_val-1] == ' '):

                    self.clear_barbarian(grid)

                    self.set_x(x_val-1)
                    self.update_barbarian_stats(grid)
                else:
                    strike(x_val-1, y_val, self.attack_damage, grid, Town_hall)
        else:
            if(y_diff > 0):
                if(grid[y_val+1][x_val] == ' '):

                    self.clear_barbarian(grid)

                    self.set_y(y_val+1)
                    self.update_barbarian_stats(grid)
                else:
                    strike(x_val, y_val+1, self.attack_damage, grid, Town_hall)
            if(y_diff < 0):
                if(grid[y_val-1][x_val] == ' '):

                    self.clear_barbarian(grid)

                    self.set_y(y_val-1)
                    self.update_barbarian_stats(grid)
                else:
                    strike(x_val, y_val-1, self.attack_damage, grid, Town_hall)


class Baloon(Troops):
    def __init__(self, x, y):
        self.max_health = 80
        self.health = 80
        self.attack_damage = 40
        super().__init__(x, y)

    def place_baloon(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = Back.LIGHTCYAN_EX + Fore.BLACK + "!" + Style.RESET_ALL

    def clear_baloon(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = " "

    def update_baloon_stats(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.health > 50):
            grid[y][x] = Back.LIGHTCYAN_EX + Fore.BLACK + "!" + Style.RESET_ALL
        elif(self.health > 20):
            grid[y][x] = Back.LIGHTYELLOW_EX + \
                Fore.BLACK + "!" + Style.RESET_ALL
        elif(self.health > 0):
            grid[y][x] = Back.LIGHTRED_EX + Fore.BLACK + "!" + Style.RESET_ALL
        else:
            self.clear_baloon(grid)

    def update_baloon(self, grid, Town_hall):
        min_dist = 100
        flag = -1
        index = -1

        for i in range(len(Cannon_arr)):
            x_dist = Cannon_arr[i].get_x() - self.get_x()
            y_dist = Cannon_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 2
                index = i
                min_dist = dist

        for i in range(len(Wizard_tower_arr)):
            x_dist = Wizard_tower_arr[i].get_x() - self.get_x()
            y_dist = Wizard_tower_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 4
                index = i
                min_dist = dist

        if(min_dist == 100):

            for i in range(len(Huts_arr)):
                x_dist = Huts_arr[i].get_x() - self.get_x()
                y_dist = Huts_arr[i].get_y() - self.get_y()

                dist = math.sqrt(x_dist**2 + y_dist**2)
                if(dist < min_dist):
                    flag = 1
                    index = i
                    min_dist = dist

            if(Town_hall.destroyed == 0):
                TH_x_dist = Town_hall.get_x() - self.get_x()
                TH_y_dist = Town_hall.get_y() - self.get_y()

                dist = math.sqrt(TH_x_dist**2 + TH_y_dist**2)
                if(dist < min_dist):
                    flag = 3
                    min_dist = dist

        # print('flagg',flag)
        x_val = self.get_x()
        y_val = self.get_y()

        x_diff = 0
        y_diff = 0

        if(flag == 1):
            x_diff = Huts_arr[index].get_x() - x_val
            y_diff = Huts_arr[index].get_y() - y_val

        if(flag == 2):
            x_diff = Cannon_arr[index].get_x() - x_val
            y_diff = Cannon_arr[index].get_y() - y_val

        if(flag == 3):
            x_diff = Town_hall.get_x()+1 - x_val
            y_diff = Town_hall.get_y()+1 - y_val

        if(flag == 4):
            x_diff = Wizard_tower_arr[index].get_x() - x_val
            y_diff = Wizard_tower_arr[index].get_y() - y_val

        if(x_diff == 0 and y_diff == 0):
            if(flag == 1):
                Huts_arr[index].health -= self.attack_damage
                Huts_arr[index].update_hut(grid)
                if(Huts_arr[index].health <= 0):
                    Huts_arr[index].clear(grid)
                    Huts_arr.pop(index)
            if(flag == 2):
                Cannon_arr[index].health -= self.attack_damage
                Cannon_arr[index].update_cannon(grid)
                if(Cannon_arr[index].health <= 0):
                    Cannon_arr[index].clear_cannon(grid)
                    Cannon_arr.pop(index)

            if(flag == 3):
                Town_hall.health -= self.attack_damage
                Town_hall.update_TH(grid)
                if(Town_hall.health <= 0):
                    Town_hall.clear(grid)
                    Town_hall.destroyed = 1

            if(flag == 4):
                Wizard_tower_arr[index].health -= self.attack_damage
                Wizard_tower_arr[index].update_wizard_tower(grid)
                if(Wizard_tower_arr[index].health <= 0):
                    Wizard_tower_arr[index].clear_wizard_tower(grid)
                    Wizard_tower_arr.pop(index)

        elif(abs(x_diff) > abs(y_diff)):
            if(x_diff > 0):
                self.clear_baloon(grid)
                self.set_x(x_val+1)
                self.update_baloon_stats(grid)
            if(x_diff < 0):
                self.clear_baloon(grid)
                self.set_x(x_val-1)
                self.update_baloon_stats(grid)
        else:
            if(y_diff > 0):
                self.clear_baloon(grid)
                self.set_y(y_val+1)
                self.update_baloon_stats(grid)
            if(y_diff < 0):
                self.clear_baloon(grid)
                self.set_y(y_val-1)
                self.update_baloon_stats(grid)


class Archer(Troops):
    def __init__(self, x, y):
        self.max_health = 40
        self.health = 40
        self.attack_damage = 10
        super().__init__(x, y)

    def place_archer(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = Back.LIGHTYELLOW_EX + Fore.BLACK + "A" + Style.RESET_ALL

    def clear_archer(self, grid):
        x = self.get_x()
        y = self.get_y()

        grid[y][x] = " "

    def update_archer_stats(self, grid):
        x = self.get_x()
        y = self.get_y()

        if(self.health > self.max_health/2):
            grid[y][x] = Back.LIGHTYELLOW_EX + \
                Fore.BLACK + "A" + Style.RESET_ALL
        elif(self.health > self.max_health/4):
            grid[y][x] = Back.YELLOW + \
                Fore.BLACK + "A" + Style.RESET_ALL
        elif(self.health > 0):
            grid[y][x] = Back.LIGHTRED_EX + Fore.BLACK + "A" + Style.RESET_ALL
        else:
            self.clear_archer(grid)

    def update_archer(self, grid, Town_hall):
        min_dist = 100
        flag = -1
        index = -1

        for i in range(len(Huts_arr)):
            x_dist = Huts_arr[i].get_x() - self.get_x()
            y_dist = Huts_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 1
                index = i
                min_dist = dist

        for i in range(len(Cannon_arr)):
            x_dist = Cannon_arr[i].get_x() - self.get_x()
            y_dist = Cannon_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 2
                index = i
                min_dist = dist

        for i in range(len(Wizard_tower_arr)):
            x_dist = Wizard_tower_arr[i].get_x() - self.get_x()
            y_dist = Wizard_tower_arr[i].get_y() - self.get_y()

            dist = math.sqrt(x_dist**2 + y_dist**2)
            if(dist < min_dist):
                flag = 4
                index = i
                min_dist = dist

        if(Town_hall.destroyed == 0):
            TH_x_dist = Town_hall.get_x() - self.get_x()
            TH_y_dist = Town_hall.get_y() - self.get_y()

            dist = math.sqrt(TH_x_dist**2 + TH_y_dist**2)
            if(dist < min_dist):
                flag = 3
                min_dist = dist

        if(min_dist <= 5):
            if(flag == 1):
                Huts_arr[index].health -= self.attack_damage
                Huts_arr[index].update_hut(grid)
                if(Huts_arr[index].health <= 0):
                    Huts_arr[index].clear(grid)
                    Huts_arr.pop(index)
            if(flag == 2):
                Cannon_arr[index].health -= self.attack_damage
                Cannon_arr[index].update_cannon(grid)
                if(Cannon_arr[index].health <= 0):
                    Cannon_arr[index].clear_cannon(grid)
                    Cannon_arr.pop(index)

            if(flag == 3):
                Town_hall.health -= self.attack_damage
                Town_hall.update_TH(grid)
                if(Town_hall.health <= 0):
                    Town_hall.clear(grid)
                    Town_hall.destroyed = 1

            if(flag == 4):
                Wizard_tower_arr[index].health -= self.attack_damage
                Wizard_tower_arr[index].update_wizard_tower(grid)
                if(Wizard_tower_arr[index].health <= 0):
                    Wizard_tower_arr[index].clear_wizard_tower(grid)
                    Wizard_tower_arr.pop(index)
        else:

            # print('flagg',flag)
            x_val = self.get_x()
            y_val = self.get_y()

            x_diff = 0
            y_diff = 0

            if(flag == 1):
                x_diff = Huts_arr[index].get_x() - x_val
                y_diff = Huts_arr[index].get_y() - y_val

            if(flag == 2):
                x_diff = Cannon_arr[index].get_x() - x_val
                y_diff = Cannon_arr[index].get_y() - y_val

            if(flag == 3):
                x_diff = Town_hall.get_x()+1 - x_val
                y_diff = Town_hall.get_y()+1 - y_val

            if(flag == 4):
                x_diff = Wizard_tower_arr[index].get_x() - x_val
                y_diff = Wizard_tower_arr[index].get_y() - y_val

            if(abs(x_diff) > abs(y_diff)):
                if(x_diff > 0):
                    if(grid[y_val][x_val+1] == ' '):

                        self.clear_archer(grid)

                        self.set_x(x_val+1)
                        self.update_archer_stats(grid)
                    else:
                        strike(x_val+1, y_val, self.attack_damage,
                               grid, Town_hall)
                if(x_diff < 0):
                    if(grid[y_val][x_val-1] == ' '):

                        self.clear_archer(grid)

                        self.set_x(x_val-1)
                        self.update_archer_stats(grid)
                    else:
                        strike(x_val-1, y_val, self.attack_damage,
                               grid, Town_hall)
            else:
                if(y_diff > 0):
                    if(grid[y_val+1][x_val] == ' '):

                        self.clear_archer(grid)

                        self.set_y(y_val+1)
                        self.update_archer_stats(grid)
                    else:
                        strike(x_val, y_val+1, self.attack_damage,
                               grid, Town_hall)
                if(y_diff < 0):
                    if(grid[y_val-1][x_val] == ' '):

                        self.clear_archer(grid)

                        self.set_y(y_val-1)
                        self.update_archer_stats(grid)
                    else:
                        strike(x_val, y_val-1, self.attack_damage,
                               grid, Town_hall)
