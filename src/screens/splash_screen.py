from .screen import Screen


class SplashScreen(Screen):

    def __init__(self):
        super().__init__()

    def draw(self, subheading):
        self.clear()

        # Print some empty lines for spacing.
        for _ in range(10):
            print('\n')

        # Draw Heading.
        self.draw_subheading(subheading)


