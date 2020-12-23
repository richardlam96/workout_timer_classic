from ..helpers.prettyprint import *
import os


class Screen(object):

    def __init__(self, heading, subheading, description=""):
        self.heading = heading
        self.subheading = subheading
        self.description = description

    def draw(self):
        self.clear()
        pprint_heading(self.heading, font="sub-zero")
        pprint_subheading(self.subheading, font="sub-zero")
        pprint_center(self.description)

    def clear(self):
        os.system('clear')

