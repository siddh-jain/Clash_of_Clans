
from colorama import init, Fore, Back, Style
from matplotlib.pyplot import grid

init()


class Map:
    # Creating the map for the game
    def __init__(self, rows, columns):
        self.__columns = columns
        self.__rows = rows
        self.grid = []

    # For creating map
    def create_map(self):
        for i in range(self.__rows):
            self.temp = []
            for j in range(self.__columns):
                if(i == 0 or j == 0 or i == self.__rows - 1 or j == self.__columns-1):
                    self.temp.append("X")
                else:
                    self.temp.append(" ")
            self.grid.append(self.temp)

    # For Printing map
    def print_map(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                # colour
                print(Fore.BLACK+Back.LIGHTGREEN_EX +
                      self.grid[i][j]+Style.RESET_ALL, end='')
                # print(self.grid[i][j],end='')

            print()

    def clear_map(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if(i == 0 or j == 0 or i == self.__rows - 1 or j == self.__columns-1):
                    self.grid[i][j] = "X"
                else:
                    self.grid[i][j] = " "
