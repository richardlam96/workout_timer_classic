import os
from config import WORKOUT_FILES
from src.screens.menu_screen import MenuScreen
from src.helpers.filehelper import read_list


class Engine(object):

    def __init__(self):
        pass

    def start(self):
        workout_list = os.listdir(WORKOUT_FILES)
        intro_menu = MenuScreen("Interval Timer!", "My App", workout_list)
