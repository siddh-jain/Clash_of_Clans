from src.headers import *
from src.initialise import *
from src.buildings import *
from src.troops import *
from src.spells import *
import datetime


def handle_inputs(replay, frame):
    if(replay == 0):
        input_char = input_to(Get_char)
        input_keys.append(input_char)

    if(replay == 1):
        input_char = new_input_to(Get_char, keys, frame)
        sleep(INPUT_TIME)

    if(input_char == 'q'):
        quit()
    if(Hero.alive == 1):
        if(input_char == 'w'):
            Hero.move_up(Village_Map.grid)
        if(input_char == 's'):
            Hero.move_down(Village_Map.grid)
        if(input_char == 'a'):
            Hero.move_left(Village_Map.grid)
        if(input_char == 'd'):
            Hero.move_right(Village_Map.grid)
        if(input_char == ' '):
            Hero.attack(Village_Map.grid, Town_hall)
        if(input_char == 'e' and hasattr(Hero, 'attack_radius')):
            QueenEagleEye.append(frame)
            Hero.eagle_arrow_attack(Village_Map.grid, Town_hall)

    # Spawning troops
    if(input_char == '1' and Spawn_arr[0].barbarians > 0):
        Barbarian_arr.append(
            Barbarian(Spawn_arr[0].get_x(), Spawn_arr[0].get_y()))
        Spawn_arr[0].barbarians -= 1
    if(input_char == '2' and Spawn_arr[1].barbarians > 0):
        Barbarian_arr.append(
            Barbarian(Spawn_arr[1].get_x(), Spawn_arr[1].get_y()))
        Spawn_arr[1].barbarians -= 1
    if(input_char == '3' and Spawn_arr[2].barbarians > 0):
        Barbarian_arr.append(
            Barbarian(Spawn_arr[2].get_x(), Spawn_arr[2].get_y()))
        Spawn_arr[2].barbarians -= 1
    if(input_char == '4' and Spawn_arr[0].baloons > 0):
        Baloon_arr.append(
            Baloon(Spawn_arr[0].get_x(), Spawn_arr[0].get_y()))
        Spawn_arr[0].baloons -= 1
    if(input_char == '5' and Spawn_arr[1].baloons > 0):
        Baloon_arr.append(
            Baloon(Spawn_arr[1].get_x(), Spawn_arr[1].get_y()))
        Spawn_arr[1].baloons -= 1
    if(input_char == '6' and Spawn_arr[2].baloons > 0):
        Baloon_arr.append(
            Baloon(Spawn_arr[2].get_x(), Spawn_arr[2].get_y()))
        Spawn_arr[2].baloons -= 1
    if(input_char == '7' and Spawn_arr[0].archers > 0):
        Archer_arr.append(
            Archer(Spawn_arr[0].get_x(), Spawn_arr[0].get_y()))
        Spawn_arr[0].archers -= 1
    if(input_char == '8' and Spawn_arr[1].archers > 0):
        Archer_arr.append(
            Archer(Spawn_arr[1].get_x(), Spawn_arr[1].get_y()))
        Spawn_arr[1].archers -= 1
    if(input_char == '9' and Spawn_arr[2].archers > 0):
        Archer_arr.append(
            Archer(Spawn_arr[2].get_x(), Spawn_arr[2].get_y()))
        Spawn_arr[2].archers -= 1

    # print(heal.number)
    if(input_char == 'h' and heal.number > 0):
        heal.cast_spell(Hero)
        heal.number -= 1
    if(input_char == 'r' and rage.number > 0 and rage.active == 0):
        rage.cast_spell(frame)
        rage.number -= 1


def Check_building_status():

    for wall in Walls_arr:
        wall.update_wall(Village_Map.grid)
        if(wall.health <= 0):
            Walls_arr.remove(wall)

    for cannon in Cannon_arr:
        cannon.update_cannon(Village_Map.grid)
        if(cannon.health <= 0):
            Cannon_arr.remove(cannon)

    for wizard_tower in Wizard_tower_arr:
        wizard_tower.update_wizard_tower(Village_Map.grid)
        if(wizard_tower.health <= 0):
            Wizard_tower_arr.remove(wizard_tower)

    for hut in Huts_arr:
        hut.update_hut(Village_Map.grid)
        if(hut.health <= 0):
            Huts_arr.remove(hut)

    if(Town_hall.destroyed == 0):
        Town_hall.update_TH(Village_Map.grid)
        if(Town_hall.health <= 0):
            Town_hall.destroyed = 1

    for i in range(len(Spawn_arr)):
        Spawn_arr[i].place_spawner(Village_Map.grid)


def UpdateBarbarians():
    for barb in Barbarian_arr:
        barb.update_barb(Village_Map.grid, Town_hall)
        barb.update_barbarian_stats(Village_Map.grid)
        # print(barb.get_x(),barb.get_y())


def UpdateArchers():
    for archer in Archer_arr:
        archer.update_archer(Village_Map.grid, Town_hall)
        archer.update_archer_stats(Village_Map.grid)


def UpdateBaloons():
    for baloon in Baloon_arr:
        baloon.update_baloon(Village_Map.grid, Town_hall)
        baloon.update_baloon_stats(Village_Map.grid)


def PlaceBaloons():
    for baloon in Baloon_arr:
        baloon.update_baloon_stats(Village_Map.grid)


def FireCannons():
    for cannon in Cannon_arr:
        cannon.fire_cannon(Village_Map.grid, Hero)


def FireWizardTowers():
    for tower in Wizard_tower_arr:
        tower.fire_wizard_tower(Village_Map.grid, Hero)


def CheckSpells(frame):
    if(rage.active == 1):
        if(frame == rage.start + rage._time * FRAME_RATE):
            rage.active = 0


def printData():
    # for hut in Huts_arr:
    #     x = hut.get_x()
    #     y = hut.get_y()
    #     print('hut-', x, y)

    # for cannon in Cannon_arr:
    #     x = cannon.get_x()
    #     y = cannon.get_y()
    #     print('canon-', x, y)

    # for wall in Walls_arr:
    #     x = wall.get_x()
    #     y = wall.get_y()
    #     print('('+str(x)+','+str(y)+')', end=' ')

    print("barbs--", len(Barbarian_arr), "---")


def Update(frame, level):
    CheckSpells(frame)
    if(frame % 3 == 0):
        FireCannons()

    if(frame % 3 == 1):
        FireWizardTowers()

    if(frame % 2 == 0 and rage.active == 0):
        UpdateBarbarians()

    UpdateArchers()
    UpdateBaloons()

    if(rage.active == 1):
        UpdateBarbarians()
        UpdateArchers()
        UpdateBaloons()

    if(len(QueenEagleEye) > 0 and QueenEagleEye[0] + FRAME_RATE == frame):
        EagleArrow(QueenEagleEye[1], QueenEagleEye[2],
                   QueenEagleEye[3], Town_hall)
        QueenEagleEye.clear()

    Check_building_status()
    PlaceBaloons()
    place_cursor(0, 0)
    show_head(level)
    Village_Map.print_map()
    # printData()


def save_keys(input_keys):
    current_time = datetime.datetime.now()
    path = "replays/" + str(current_time) + ".txt"
    output_file = open(path, 'w')

    if(hasattr(Hero, 'attack_radius')):
        output_file.write("queen" + '\n')
    else:
        output_file.write("king" + '\n')

    for key in input_keys:
        output_file.write(str(key) + '\n')
    output_file.close()


def Create_level_2():

    Walls_arr.clear()
    Barbarian_arr.clear()
    Archer_arr.clear()
    Baloon_arr.clear()

    # print(len(Barbarian_arr))

    Village_Map.clear_map()

    Town_hall.place_TH(Village_Map.grid)
    Town_hall.health = Town_hall.max_health
    Town_hall.destroyed = 0

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

    walls_x_min = round(WIDTH/2) - 5
    walls_x_max = round(WIDTH/2) + 5
    walls_y_min = round(HEIGHT/2) + 5
    walls_y_max = round(HEIGHT/2) + 9

    for i in range(walls_x_min, walls_x_max+1):
        Walls_arr.append(Walls(i, walls_y_max))

    for i in range(walls_y_min, walls_y_max):
        Walls_arr.append(Walls(walls_x_min, i))
        Walls_arr.append(Walls(walls_x_max, i))

    for i in range(len(Walls_arr)):
        Walls_arr[i].place_wall(Village_Map.grid)

    walls_x_min = 68 - 3
    walls_x_max = 68 + 3
    walls_y_min = 13 - 2
    walls_y_max = 18 + 2

    for i in range(walls_x_min, walls_x_max+1):
        Walls_arr.append(Walls(i, walls_y_min))
        Walls_arr.append(Walls(i, walls_y_max))

    for i in range(walls_y_min, walls_y_max):
        Walls_arr.append(Walls(walls_x_min, i))
        Walls_arr.append(Walls(walls_x_max, i))

    # Cannons
    Cannon_arr.append(Cannon(43, 17))
    Cannon_arr.append(Cannon(68, 13))
    Cannon_arr.append(Cannon(50, 22))

    for i in range(len(Cannon_arr)):
        Cannon_arr[i].place_cannon(Village_Map.grid)

    # Wizard Tower
    Wizard_tower_arr.append(Wizard_Tower(68, 17))
    Wizard_tower_arr.append(Wizard_Tower(44, 9))
    Wizard_tower_arr.append(Wizard_Tower(34, 13))

    for i in range(len(Wizard_tower_arr)):
        Wizard_tower_arr[i].place_wizard_tower(Village_Map.grid)

    Hero.set_x(4)
    Hero.set_y(2)
    Hero.health = Hero.max_health
    Hero.alive = 1
    Hero.place_hero(Village_Map.grid)

    for i in range(len(Spawn_arr)):
        Spawn_arr[i].barbarians = 10
        Spawn_arr[i].archers = 8
        Spawn_arr[i].baloons = 3

    heal.number = 2
    rage.number = 2


def Create_level_3():

    Walls_arr.clear()
    Barbarian_arr.clear()
    Archer_arr.clear()
    Baloon_arr.clear()
    Wizard_tower_arr.clear()
    Cannon_arr.clear()

    Village_Map.clear_map()

    Town_hall.place_TH(Village_Map.grid)
    Town_hall.health = Town_hall.max_health
    Town_hall.destroyed = 0

    Huts_arr.append(Hut(48, 18))
    Huts_arr.append(Hut(82, 21))
    Huts_arr.append(Hut(25, 24))
    Huts_arr.append(Hut(15, 10))
    Huts_arr.append(Hut(60, 5))
    Huts_arr.append(Hut(48, 11))
    Huts_arr.append(Hut(37, 16))

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

    walls_x_min = round(WIDTH/2) - 5
    walls_x_max = round(WIDTH/2) + 5
    walls_y_min = round(HEIGHT/2) + 5
    walls_y_max = round(HEIGHT/2) + 9

    for i in range(walls_x_min, walls_x_max+1):
        Walls_arr.append(Walls(i, walls_y_max))

    for i in range(walls_y_min, walls_y_max):
        Walls_arr.append(Walls(walls_x_min, i))
        Walls_arr.append(Walls(walls_x_max, i))

    walls_x_min = 61 - 3
    walls_x_max = 61 + 3
    walls_y_min = 16 - 2
    walls_y_max = 17 + 2

    for i in range(walls_x_min, walls_x_max+1):
        Walls_arr.append(Walls(i, walls_y_min))
        Walls_arr.append(Walls(i, walls_y_max))

    for i in range(walls_y_min, walls_y_max):
        Walls_arr.append(Walls(walls_x_max, i))

    walls_x_min = round(WIDTH/2) - 9
    walls_x_max = round(WIDTH/2) + 6
    walls_y_min = round(HEIGHT/2) - 6
    walls_y_max = round(HEIGHT/2) - 2

    for i in range(walls_x_min, walls_x_max+1):
        Walls_arr.append(Walls(i, walls_y_min))

    for i in range(walls_y_min, walls_y_max):
        Walls_arr.append(Walls(walls_x_min, i))
        Walls_arr.append(Walls(walls_x_max, i))

    walls_x_min = 37 - 2
    walls_x_max = 37 + 2
    walls_y_min = 16 - 2
    walls_y_max = 16 + 2

    for i in range(walls_x_min, walls_x_max+1):
        Walls_arr.append(Walls(i, walls_y_min))
        Walls_arr.append(Walls(i, walls_y_max))

    for i in range(walls_y_min, walls_y_max):
        Walls_arr.append(Walls(walls_x_min, i))

    for i in range(len(Walls_arr)):
        Walls_arr[i].place_wall(Village_Map.grid)

    # Cannons
    Cannon_arr.append(Cannon(43, 18))
    Cannon_arr.append(Cannon(61, 15))
    Cannon_arr.append(Cannon(50, 23))
    Cannon_arr.append(Cannon(45, 11))

    for i in range(len(Cannon_arr)):
        Cannon_arr[i].place_cannon(Village_Map.grid)

    # Wizard Tower
    Wizard_tower_arr.append(Wizard_Tower(61, 18))
    Wizard_tower_arr.append(Wizard_Tower(43, 15))
    Wizard_tower_arr.append(Wizard_Tower(50, 21))
    Wizard_tower_arr.append(Wizard_Tower(52, 11))

    for i in range(len(Wizard_tower_arr)):
        Wizard_tower_arr[i].place_wizard_tower(Village_Map.grid)

    Hero.set_x(4)
    Hero.set_y(2)
    Hero.health = Hero.max_health
    Hero.alive = 1
    Hero.place_hero(Village_Map.grid)

    for i in range(len(Spawn_arr)):
        Spawn_arr[i].barbarians = 10
        Spawn_arr[i].archers = 10
        Spawn_arr[i].baloons = 5

    heal.number = 3
    rage.number = 3


def Game_status(level, frame):
    # print(frame,"fr")
    if(frame == 1):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(level1_sign)):
            for j in range(x, x+len(level1_sign[0])):
                Village_Map.grid[i][j] = Back.YELLOW+Fore.BLACK + \
                    level1_sign[i-y][j-x] + Style.RESET_ALL

    if(frame == FRAME_RATE*1.5):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(level1_sign)):
            for j in range(x, x+len(level1_sign[0])):
                Village_Map.grid[i][j] = " "

    # level 2
    if(level == 1 and len(Cannon_arr) == 0 and len(Huts_arr) == 0 and len(Wizard_tower_arr) == 0 and Town_hall.destroyed == 1):
        Create_level_2()
        level = 2
        global lvl2_start
        lvl2_start = frame

    if(frame == lvl2_start):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(level2_sign)):
            for j in range(x, x+len(level2_sign[0])):
                Village_Map.grid[i][j] = Back.YELLOW+Fore.BLACK + \
                    level2_sign[i-y][j-x] + Style.RESET_ALL

    if(frame == lvl2_start + FRAME_RATE*1.5):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(level2_sign)):
            for j in range(x, x+len(level2_sign[0])):
                Village_Map.grid[i][j] = " "

    # level 3
    if(level == 2 and len(Cannon_arr) == 0 and len(Huts_arr) == 0 and len(Wizard_tower_arr) == 0 and Town_hall.destroyed == 1):
        Create_level_3()
        level = 3
        global lvl3_start
        lvl3_start = frame

    if(frame == lvl3_start):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(level3_sign)):
            for j in range(x, x+len(level3_sign[0])):
                Village_Map.grid[i][j] = Back.YELLOW+Fore.BLACK + \
                    level3_sign[i-y][j-x] + Style.RESET_ALL

    if(frame == lvl3_start + FRAME_RATE*1.5):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(level3_sign)):
            for j in range(x, x+len(level3_sign[0])):
                Village_Map.grid[i][j] = " "

    # victory
    if(level == 3 and len(Cannon_arr) == 0 and len(Huts_arr) == 0 and Town_hall.destroyed == 1):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(victory_sign)):
            for j in range(x, x+len(victory_sign[0])):
                Village_Map.grid[i][j] = Back.GREEN+Fore.BLACK + \
                    victory_sign[i-y][j-x] + Style.RESET_ALL
        show_head(level)
        Village_Map.print_map()
        if(if_replay == 0):
            save_keys(input_keys)
        quit()

    # defeat
    if(Hero.alive == 0 and Spawn_arr[0].barbarians == 0 and Spawn_arr[1].barbarians == 0 and Spawn_arr[2].barbarians == 0 and len(Barbarian_arr) == 0
       and Spawn_arr[0].archers == 0 and Spawn_arr[1].archers == 0 and Spawn_arr[2].archers == 0 and len(Archer_arr) == 0
       and Spawn_arr[0].baloons == 0 and Spawn_arr[1].baloons == 0 and Spawn_arr[2].baloons == 0 and len(Baloon_arr) == 0):
        x = 30
        y = 2
        place_cursor(0, 0)
        for i in range(y, y+len(defeat_sign)):
            for j in range(x, x+len(defeat_sign[0])):
                Village_Map.grid[i][j] = Back.LIGHTRED_EX + \
                    Fore.BLACK + defeat_sign[i-y][j-x] + Style.RESET_ALL
        show_head(level)
        Village_Map.print_map()
        if(if_replay == 0):
            save_keys(input_keys)
        quit()

    return level


def place_cursor(x, y):
    print("\033[%d;%dH" % (x, y))


def show_head(level):
    print(Fore.RED+Back.LIGHTYELLOW_EX + Style.BRIGHT +
          "Clash of Clans".center(WIDTH) + Style.RESET_ALL)
    health = ""
    if(hasattr(Hero, 'attack_radius')):
        health += " | Queens's Health: ["
    else:
        health += " | Kings's Health: ["
    bar_len = math.ceil(Hero.health/(Hero.max_health/10))
    # print(bar_len,Hero.health)
    for i in range(bar_len):
        health += "#"
    for i in range(10-bar_len):
        health += " "
    health += "]"
    if(Hero.alive == 0):
        health += " :("

    stats1 = ""
    lvl = "Level:" + str(level)

    spells = " | Heal:"+str(heal.number) + " | Rage:" + str(rage.number)
    if(rage.active == 1):
        spells += " (active)"

    eagle_arr = ""
    if(hasattr(Hero, 'attack_radius')):
        if(len(QueenEagleEye) == 0):
            eagle_arr += " | Eagle Arrow: Available"
        else:
            eagle_arr += " | Eagle Arrow: Not available"

    stats1 = lvl + health + spells + eagle_arr
    print(Back.LIGHTCYAN_EX+Fore.BLACK+stats1.center(WIDTH)+Style.RESET_ALL)

    stats2 = ""
    units = "Spawn point 1 --- Barbarians:" + str(Spawn_arr[0].barbarians)+" | Baloons:" + str(
        Spawn_arr[0].baloons) + " | Archers:" + str(Spawn_arr[0].archers)

    stats2 = units

    print(Back.LIGHTBLUE_EX+Fore.BLACK+stats2.center(WIDTH)+Style.RESET_ALL)

    stats3 = ""
    units = "Spawn point 2 --- Barbarians:" + str(Spawn_arr[1].barbarians)+" | Baloons:" + str(
        Spawn_arr[1].baloons) + " | Archers:" + str(Spawn_arr[1].archers)

    stats3 = units

    print(Back.LIGHTBLUE_EX+Fore.BLACK+stats3.center(WIDTH)+Style.RESET_ALL)

    stats4 = ""
    units = "Spawn point 3 --- Barbarians:" + str(Spawn_arr[2].barbarians)+" | Baloons:" + str(
        Spawn_arr[2].baloons) + " | Archers:" + str(Spawn_arr[2].archers)

    stats4 = units

    print(Back.LIGHTBLUE_EX+Fore.BLACK+stats4.center(WIDTH)+Style.RESET_ALL)
