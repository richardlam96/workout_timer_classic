from .screen import Screen


class MenuScreen(Screen):

    def __init__(self):
        super().__init__()

    def draw(self, heading, options_list, current_selection_index=0):
        self.clear()

        # Draw Heading and Menu List.
        self.draw_border()
        self.draw_heading(heading)
        self.draw_border()
        # pprint_menu_list(options_list, current_selection_index)
        self.draw_list(options_list, current_selection_index)

    def draw_list(self, options_list, current_selection_index=0):
        print(self.formatter
              .format_list(options_list)
              .add_numbering()
              .center()
              .color(self.primary_color, current_selection_index, attrs=['reverse', 'blink'])
              .get_as_string())

    def get_selection(self, heading, options_list, current_selection_index=0):
        selected_number = int(input("Choose workout: "))
        index = selected_number - 1

        while options_list[index] is None:
            selected_number = input("Invalid number, try again: ").rstrip('\n')

        # Redraw screen with selection and ask to confirm.
        self.draw(heading, options_list, selected_number - 1)
        input("Press 'Enter' to continue...")

        return options_list[index]

