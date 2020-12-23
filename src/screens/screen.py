import shutil
from config import *
from src.helpers.formatter import Formatter


class Screen(object):

    def __init__(self,
                 primary_font=PRIMARY_FONT,
                 secondary_font=SECONDARY_FONT,
                 primary_color=PRIMARY_COLOR,
                 secondary_color=SECONDARY_COLOR):
        self.primary_font = primary_font
        self.secondary_font = secondary_font
        self.primary_color = primary_color
        self.secondary_color = secondary_color

        self.formatter = Formatter()

    def draw_heading(self, heading):
        # Draw Heading.
        print(self.formatter
              .format_text_art(heading, font=self.primary_font)
              .color(self.primary_color)
              .center()
              .get_as_string())

    def draw_subheading(self, subheading):
        print(self.formatter
              .format_text_art(subheading, font=self.secondary_font)
              .color(self.secondary_color)
              .center()
              .get_as_string())

    def draw_border(self, border_char="="):
        terminal_width = shutil.get_terminal_size().columns
        border = [border_char * terminal_width]
        print(self.formatter
              .format_list(border)
              .color(self.secondary_color, attrs=['reverse'])
              .get_as_string())

    def clear(self):
        os.system('clear')

