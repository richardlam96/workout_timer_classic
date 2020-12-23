from ..helpers.prettyprint import *
import os


class Screen(object):

    def __init__(self, heading, subheading, description=""):
        self.heading = heading
        self.subheading = subheading
        self.description = description

    def draw(self, border_color="white"):
        self.clear()
        # Heading.
        pprint_border("=", border_color, attrs=['reverse'])
        pprint_heading(self.heading, font="sub-zero")
        pprint_border("=", border_color, attrs=['reverse'])
        print()

        pprint_subheading(self.subheading, font="graffiti")
        pprint_center(self.description)

    def clear(self):
        os.system('clear')

