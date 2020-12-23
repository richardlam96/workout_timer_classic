from ..helpers.prettyprint import *
from .screen import Screen


class MenuScreen(Screen):

    def __init__(self, heading, subheading, description, options_list):
        super().__init__(heading, subheading, description)
        self.options_list = options_list
        self.current_selection = 0
        self.draw()

    def draw(self):
        super().draw()
        pprint_menu_list(self.options_list, self.current_selection)

    def get_selection(self):
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
            elif key == '':
                break

        return self.options_list[self.current_selection]
