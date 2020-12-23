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

