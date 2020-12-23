from ..helpers.prettyprint import *
import os


class Screen(object):

    def __init__(self, heading, subheading, description=""):
        self.heading = heading
        self.subheading = subheading
        self.description = description

    def draw(self, heading_color="white", subheading_color="white", border_color="white"):
        self.clear()
        # Heading.
        if self.heading is not None:
            pprint_border("=", border_color, attrs=['reverse'])
            pprint_heading(self.heading, heading_color, font="sub-zero")
            pprint_border("=", border_color, attrs=['reverse'])
            print()

        if self.subheading is not None:
            pprint_heading(self.subheading, subheading_color, font="graffiti")

        if self.description is not None:
            pprint_center(self.description)

    def clear(self):
        os.system('clear')

