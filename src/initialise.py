from src.headers import *
from src.village import *
from src.buildings import *
from src.input import *
from src.troops import *
from src.spells import *
import time
import os

time_completed = time.time()
os.system('clear')

Get_char = Get()


# Village map
Village_Map = Map(HEIGHT, WIDTH)
Village_Map.create_map()

# Town Hall
# Town_hall = TownHall(round(WIDTH/2), round(HEIGHT/2))
Town_hall = TownHall(round(WIDTH/2), round(HEIGHT/2))
Town_hall.place_TH(Village_Map.grid)

# Huts
Huts_arr.append(Hut(45, 15))
Huts_arr.append(Hut(85, 20))
Huts_arr.append(Hut(25, 24))
Huts_arr.append(Hut(15, 10))
Huts_arr.append(Hut(60, 5))

for i in range(len(Huts_arr)):
    Huts_arr[i].place_hut(Village_Map.grid)

# Walls
walls_x_min = round(WIDTH/2) - 11
walls_x_max = round(WIDTH/2) + 8
walls_y_min = round(HEIGHT/2) - 2
walls_y_max = round(HEIGHT/2) + 5

for i in range(walls_x_min, walls_x_max+1):
    Walls_arr.append(Walls(i, walls_y_min))
    Walls_arr.append(Walls(i, walls_y_max))

for i in range(walls_y_min, walls_y_max):
    Walls_arr.append(Walls(walls_x_min, i))
    Walls_arr.append(Walls(walls_x_max, i))

for i in range(len(Walls_arr)):
    Walls_arr[i].place_wall(Village_Map.grid)

# Cannons
Cannon_arr.append(Cannon(43, 17))
Cannon_arr.append(Cannon(69, 13))

for i in range(len(Cannon_arr)):
    Cannon_arr[i].place_cannon(Village_Map.grid)

# Wizard Tower
Wizard_tower_arr.append(Wizard_Tower(67, 18))
Wizard_tower_arr.append(Wizard_Tower(24, 8))

for i in range(len(Wizard_tower_arr)):
    Wizard_tower_arr[i].place_wizard_tower(Village_Map.grid)

if(if_replay == 0):
    hero_chosen = input(
        "Welcome to the Clash of Clans\n1) Barbarian King\n2) Archer Queen\nEnter the number of hero you want to play as:")
    if(hero_chosen == '1'):
        hero = 1
    elif(hero_chosen == '2'):
        hero = 2
    else:
        print("Invalid input")
        quit()


# Heroes
if(hero == 1):
    Hero = King(4, 2)
if(hero == 2):
    Hero = Queen(4, 2)
Hero.place_hero(Village_Map.grid)

# Spawner
Spawn_arr.append(Spawn(83, 7, 1, 8, 3, 6))
Spawn_arr.append(Spawn(72, 25, 2, 8, 3, 6))
Spawn_arr.append(Spawn(15, 21, 3, 8, 3, 6))

for i in range(len(Spawn_arr)):
    Spawn_arr[i].place_spawner(Village_Map.grid)


# Spells
heal = Heal()
rage = Rage()
