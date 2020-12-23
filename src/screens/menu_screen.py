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

    def get_selection(self, options_list, current_selection_index=0):
        while True:
            key = input()
            if key == 'j':
                current_selection_index += 1
                current_selection_index %= len(options_list)
            if key == 'k':
                current_selection_index -= 1
                current_selection_index %= len(options_list)
            elif key == '':
                break

            # Redraw Screen and prompt input until valid Input.
            self.draw(options_list, current_selection_index)
            self.get_selection(options_list, current_selection_index)

        return options_list[current_selection_index]
