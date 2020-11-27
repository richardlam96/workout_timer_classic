from art import tprint
from ..helpers.prettyprint import *


class MenuScreen(object):

    def __init__(self, heading, description, options_list):
        self.heading = heading
        self.description = description
        self.options_list = options_list

        pprint_heading(self.heading, font="sub-zero")
        print(self.description)
        pprint_list(self.options_list)

