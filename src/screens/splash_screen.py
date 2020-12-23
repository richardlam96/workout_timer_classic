from ..helpers.prettyprint import *
from .screen import Screen


class SplashScreen(Screen):

    def __init__(self, subheading, description=""):
        super().__init__(heading=None, subheading=subheading, description=description)

    def draw(self):
        # Print some empty lines for spacing.
        for _ in range(10):
            print('\n')
        super().draw()

