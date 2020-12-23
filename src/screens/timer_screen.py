from ..helpers.prettyprint import *
from .screen import Screen


class TimerScreen(Screen):

    def __init__(self, heading, subheading, description=""):
        super().__init__(heading, subheading, description)

    def draw(self, seconds):
        super().draw()
        pprint_time(seconds)

