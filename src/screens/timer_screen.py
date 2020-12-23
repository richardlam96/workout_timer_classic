from config import TIMER_FONT
from .screen import Screen


class TimerScreen(Screen):

    def __init__(self, secondary_color=""):
        if secondary_color == "":
            super().__init__()
        else:
            super().__init__(secondary_color=secondary_color)

    def draw(self, heading, subheading, seconds):
        self.clear()

        self.draw_border()
        self.draw_heading(heading)
        self.draw_border()

        self.draw_subheading(subheading)

        self.draw_time(seconds)

    def draw_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(self.formatter
              .format_text_art(timeformat, font=TIMER_FONT)
              .color(self.primary_color)
              .center()
              .get_as_string())


