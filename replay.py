import src.headers as head
import os.path
from colorama import init, Fore, Back, Style
from time import sleep

init()

sleep(0.10)

head.if_replay = 1

if(head.if_replay == 1):
    val = input("enter the file name to be replayed:")
    path = 'replays/' + val
    file_exists = os.path.exists(path)

    if(file_exists == False):
        print("The file dosent exist")
        quit()
    # open file and read the content in a list
    with open(path, 'r') as filehandle:
        hero_name = filehandle.readline()
        for line in filehandle:
            currentPlace = line[:-1]
            # add item to the list
            head.keys.append(currentPlace)
    # print(hero_name)
    # print(head.keys)
    if(hero_name == 'king\n'):
        head.hero = 1
    elif(hero_name == 'queen\n'):
        head.hero = 2

from src.update import *


while(1):
    handle_inputs(if_replay, frame)
    Update(frame, level)
    level = Game_status(level, frame)
    frame = frame+1
    # print(frame)
