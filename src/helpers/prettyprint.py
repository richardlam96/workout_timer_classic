import shutil
from .formatter import format_heading, format_list, format_time


def pprint_heading(text, border_char="*", **kwargs):
    pprint_border(border_char)
    print(format_heading(text, **kwargs))
    pprint_border(border_char)


def pprint_list(item_list):
    print(format_list(item_list))


def pprint_time(seconds):
    print(format_time(seconds))


def pprint_border(border_char):
    terminal_width = shutil.get_terminal_size().columns
    border = border_char * terminal_width
    print(border)
