import shutil
from art import text2art
from termcolor import colored


class Formatter(object):

    def __init__(self):
        self.text_list = []

    def format_text_art(self, text, **kwargs):
        textart = text2art(text, **kwargs)
        self.text_list = textart.split('\n')
        return self

    def format_list(self, text_list):
        self.text_list = text_list
        return self

    def color(self, color, item_index=None, **kwargs):
        if item_index is None:
            self.text_list = [colored(line, color, **kwargs) for line in self.text_list]
        else:
            self.text_list[item_index] = colored(self.text_list[item_index], color, **kwargs)
        return self

    def center(self, pad_char=' '):
        # Calculate padding to apply.
        terminal_width = shutil.get_terminal_size().columns
        padding = min([terminal_width - len(line) for line in self.text_list])
        left_pad = (padding // 2) * pad_char
        # self.text_list = list(map(lambda line: left_pad + line, self.text_list))
        self.text_list = [left_pad + line for line in self.text_list]
        return self

    def add_numbering(self):
        self.text_list = ["{}) {}".format(index + 1, item)
                          for index, item in enumerate(self.text_list)]
        return self

    def get_as_list(self):
        formatted_text = self.text_list
        self.text_list = []
        return formatted_text

    def get_as_string(self):
        formatted_text = '\n'.join(self.text_list)
        self.text_list = []
        return formatted_text


def format_heading(text, **kwargs):
    formatter = Formatter()
    return formatter\
        .format_text_art(text, **kwargs)\
        .color("cyan")\
        .center()\
        .get_as_list()

    # heading = text2art(text, **kwargs)
    # centered_heading = format_center(heading)
    # return [format_color(line, "cyan") for line in centered_heading]
    # return join_to_string(centered_heading)


def format_color(text, color, **kwargs):
    return colored(text, color, **kwargs)


def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    time_art = text2art(timeformat, font='block', chr_ignore=True)
    return time_art  # Block doesn't need centering.


def format_list(item_list):
    numbered_list = add_numbering(item_list)
    padded_list = format_center(join_to_string(numbered_list))
    return join_to_string(padded_list)


def format_center(multiline_text, pad_char=' '):
    """ Centers entire message using padding. """
    # Split text into lines if applicable.
    lines = multiline_text.split('\n')

    # Calculate padding to apply.
    terminal_width = shutil.get_terminal_size().columns
    padding = min([terminal_width - len(item) for item in lines])
    left_pad = (padding // 2) * pad_char
    return list(map(lambda item: left_pad + item, lines))


def add_selection_indicator(multiline_text, selection_index):
    lines = multiline_text.split('\n')
    selected_line = colored(lines[selection_index], 'cyan', attrs=['reverse', 'blink'])
    lines[selection_index] = selected_line
    return join_to_string(lines)


def add_numbering(list_of_string):
    return ["{}) {}".format(index + 1, item)
            for index, item in enumerate(list_of_string)]


def join_to_string(list_of_string):
    return '\n'.join(list_of_string)

