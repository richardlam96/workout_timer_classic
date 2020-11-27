from ..helpers.prettyprint import *
import os


class Screen(object):

    def __init__(self, heading, subheading, description):
        self.heading = heading
        self.subheading = subheading
        self.description = description

    def draw(self):
        pprint_heading(self.heading, font="sub-zero")
        print(self.subheading)
        print(self.description)

    def clear(self):
        os.system('clear')

