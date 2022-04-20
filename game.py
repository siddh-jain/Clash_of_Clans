from src.headers import *
import os.path
from colorama import init, Fore, Back, Style
from time import sleep
from src.update import *

init()

sleep(0.10)

if_replay = 0

if(if_replay == 1):
    val = input("enter the file name to be replayed:")
    path = 'replays/' + val
    file_exists = os.path.exists(path)

    if(file_exists == False):
        print("The file dosent exist")
        quit()
    # open file and read the content in a list
    with open(path, 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            # add item to the list
            keys.append(currentPlace)


while(1):
    handle_inputs(if_replay, frame)
    Update(frame, level)
    level = Game_status(level, frame)
    frame = frame+1
    # print(frame)
