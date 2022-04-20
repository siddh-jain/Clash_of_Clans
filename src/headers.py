
HEIGHT = 30
WIDTH = 100

FRAME_RATE = 10

INPUT_TIME = 1/FRAME_RATE

Huts_arr = []
Walls_arr = []
Cannon_arr = []
Wizard_tower_arr = []
Spawn_arr = []
Barbarian_arr = []
Baloon_arr = []
Archer_arr = []
input_keys = []
if_replay = 0
keys = []
frame = 0
lvl2_start = -1000
lvl3_start = -1000
hero = -1
level = 1
QueenEagleEye = []


victory_sign = [list("         _      _                     "),
                list("        (_)    | |                    "),
                list("  __   ___  ___| |_ ___  _ __ _   _   "),
                list("  \ \ / / |/ __| __/ _ \| '__| | | |  "),
                list("   \ V /| | (__| || (_) | |  | |_| |  "),
                list("    \_/ |_|\___|\__\___/|_|   \__, |  "),
                list("                               __/ |  "),
                list("                              |___/   "),
                list("                                      ")]


defeat_sign = [list("       _       __           _     "),
               list("      | |     / _|         | |    "),
               list("    __| | ___| |_ ___  __ _| |_   "),
               list("   / _` |/ _ \  _/ _ \/ _` | __|  "),
               list("  | (_| |  __/ ||  __/ (_| | |_   "),
               list("   \__,_|\___|_| \___|\__,_|\__|  "),
               list("                                  ")]

level1_sign = [list("   _                   _   ___   "),
               list("  | |                 | | /_  |  "),
               list("  | | _____    __ ___ | |   | |  "),
               list("  | |/ _ \ \  / // _ \| |   | |  "),
               list("  | |  __/\ \/ /|  __/| |   | |  "),
               list("  |_|\___| \__/  \___||_|   |_|  "),
               list("                                 ")]


level2_sign = [list("   _                   _  _______    "),
               list("  | |                 | | \      \   "),
               list("  | | _____    __ ___ | |  \____  \  "),
               list("  | |/ _ \ \  / // _ \| |  /  ____/  "),
               list("  | |  __/\ \/ /|  __/| | /       \  "),
               list("  |_|\___| \__/  \___||_| \________\ "),
               list("                                     ")]

level3_sign = [list("   _                   _   _______   "),
               list("  | |                 | | |_____  |  "),
               list("  | | __ __    __ ___ | |  _____| |  "),
               list("  | |/ _ \ \  / // _ \| | |_____  |  "),
               list("  | |  __/\ \/ /|  __/| |  _____| |  "),
               list("  |_|\___| \__/  \___||_| |_______|  "),
               list("                                     ")]

level3_sign_old = [list("   _                   _  ________    "),
                   list("  | |                 | | \       \   "),
                   list("  | | _____    __ ___ | |  \_____  \  "),
                   list("  | |/ _ \ \  / // _ \| |   __(__  <  "),
                   list("  | |  __/\ \/ /|  __/| |  /        \ "),
                   list("  |_|\___| \__/  \___||_| /________ / "),
                   list("                                      ")]
