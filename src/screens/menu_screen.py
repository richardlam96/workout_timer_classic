from ..helpers.prettyprint import *


class MenuScreen(object):

    def __init__(self, heading, description, options_list):
        self.heading = heading
        self.description = description
        self.options_list = options_list
        self.current_selection = 0

        self.draw()
        self.wait_for_input()

    def draw(self):
        pprint_heading(self.heading, font="sub-zero")
        print(self.description)
        pprint_menu_list(self.options_list, self.current_selection)

    def wait_for_input(self):
        while True:
            key = input()
            if key == 'j':
                self.current_selection += 1
                self.draw()
            elif key == 'q':
                break

