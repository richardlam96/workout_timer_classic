from ..helpers.prettyprint import *
from .screen import Screen


class MenuScreen(Screen):

    def __init__(self, heading, description, options_list):
        self.heading = heading
        self.description = description
        self.options_list = options_list
        self.current_selection = 0

        self.draw()
        self.wait_for_input()

    def draw(self):
        self.clear()
        pprint_heading(self.heading, font="sub-zero")
        print(self.description)
        pprint_menu_list(self.options_list, self.current_selection)

    def wait_for_input(self):
        while True:
            key = input()
            if key == 'j':
                self.current_selection += 1
                self.current_selection %= len(self.options_list)
                self.draw()
            if key == 'k':
                self.current_selection -= 1
                self.current_selection %= len(self.options_list)
                self.draw()
            elif key == 'q':
                break
